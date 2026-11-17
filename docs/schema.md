# 数据结构说明

`data/cpus_db.json` 是一个顶层对象，含 8 个数组，命名规则为 `{vendor}_{table}`：

| 表 | Intel | AMD |
|---|---|---|
| 产品线 | `intel_products` | `amd_products` |
| 系列 | `intel_series` | `amd_series` |
| 型号（列表项） | `intel_cpu` | `amd_cpu` |
| 详情 | `intel_cpu_data` | `amd_cpu_data` |

层级关系：

```
products (1) ──< series (N) ──< cpu (N) ──< cpu_data (N)
   id          id_product_family   id_serie      id_cpu
```

所有值都是**字符串或 `null`**，没有 JSON 数字与布尔值。这是原库的约定，解析时统一按字符串处理再转换。

---

## 1. products — 产品线

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | str(int) | 主键，厂商内唯一 |
| `product_name` | str | 展示名，如 `Core i5`、`Ryzen 7`、`EPYC` |
| `family` | str | 小写标识，如 `corei5`、`ryzen9`、`epyc` |
| `type` | str | 平台类型，见下表 |
| `order_product` | str(int) | 同一 `type` 内的展示顺序 |

`type` 取值：

| 值 | 含义 |
|---|---|
| `dk` | Desktop 桌面 |
| `mb` | Mobile 移动 |
| `sv` | Server 服务器 |
| `ed` | Embedded 嵌入式 |
| `cs` | Custom / Console 定制 |

同一 `product_name` 在不同 `type` 下是**不同的行**（如 `Core i5` 分别存在于 `dk` 与 `mb`），这是区分桌面版与移动版的唯一依据。

---

## 2. series — 系列

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | str(int) | 主键 |
| `id_product_family` | str(int) | 外键 → `products.id` |
| `serie_name` | str | 展示名，如 `Core i5 12th Generation`、`Ryzen 7 5000 Series` |
| `order_family` | str(int) | 同一产品线内的展示顺序 |

命名沿用原库风格：Intel 用 `Core i5 {n}th Generation`，AMD 用 `Ryzen {n} {series} Series`。

---

## 3. cpu — 型号（列表项）

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | str(int) | 主键 |
| `id_serie` | str(int) | 外键 → `series.id` |
| `name` | str | 完整型号名，含厂商前缀，如 `Intel Core i9-14900K` |
| `cores` | str(int) | 核心数 |
| `core_clk` | str(int) | 基准频率，MHz |
| `core_clk_max` | str(int) | 最大频率，MHz；无睿频时等于 `core_clk` |
| `launch` | str(int) | 上市年月，格式 `YYYYMM`，如 `202310` |
| `order_number` | str(int) | 系列内展示顺序，从 1 递增 |

---

## 4. cpu_data — 详情（60 字段）

同一型号可有**多条**记录（`variant` 区分不同步进 / 封装 / 市场版本）。列表页只读 `cpu` 表，详情页按 `id_cpu` 取 `cpu_data`。

### 标识与归属

| 字段 | 说明 |
|---|---|
| `id` | 主键（独立序列，与 `cpu.id` 无关） |
| `id_cpu` | 外键 → `cpu.id` |
| `name` | 与 `cpu.name` 一致 |
| `variant` | 变体标签，无则为 `null` |

### 上市与价格

| 字段 | 说明 |
|---|---|
| `launch` | 上市时间，字符串 `Qn YYYY`，如 `Q4 2023` |
| `lauch_price` | 首发价，美元（注意原库字段名拼写为 `lauch_price`，非 `launch`） |
| `released` | `1` 已发布 / `0` 未发布或传闻（列表中以红色条提示） |

### 核心规格

| 字段 | 说明 |
|---|---|
| `cores` / `threads` | 核心数 / 线程数 |
| `core_clk` / `core_clk_boost` | 基准 / 加速频率，MHz（浮点字符串） |
| `core_clk_boost_detail` | 分核心加速描述，如 `2900:1 - 8` |
| `core_arch` | 微架构，如 `Zen 4`、`Raptor Lake`、`Arrow Lake` |
| `core_name` | 核心代号，如 `Granite Ridge`、`Genoa` |
| `core_stepping` | 步进 |
| `socket` | 插槽，如 `LGA1700`、`AM5`、`SP5` |
| `fab` | 制程，纳米 |
| `transistor_count` | 晶体管数，百万 |
| `die_size` | 核心面积，mm² |
| `pkg_size` | 封装尺寸 |
| `max_temp` | 最高工作温度，℃ |
| `vcore` | 核心电压 |
| `tdp` | 热设计功耗，W |
| `multi_cpus` | 多路支持数 |

### 缓存

单位均为 **KB**，且为**全部核心合计**（原库口径）：

| 字段 | 说明 |
|---|---|
| `cache_l1_inst` / `cache_l1_data` | 一级指令 / 数据缓存。Intel 为 `32 × 核数`；AMD Zen1–3 指令侧 `64 × 核数`、数据侧 `32 × 核数`；Zen4/5 均为 `32 × 核数` |
| `cache_l2` | 二级缓存。Intel 10 代及以前 `256 × 核数`；12 代起按 P 核 1280 / E 簇 2048 逐型号计算；AMD Zen2/3 `512 × 核数`，Zen4/5 `1024 × 核数` |
| `cache_l3` | 三级缓存 |
| `cache_l4` | 四级缓存，多数为 `null` |

### 频率相关

| 字段 | 说明 |
|---|---|
| `multiplier` / `multiplier_max` | 倍频 = 频率 / 100 |
| `multiplier_unlock` | `1` 未锁倍频（K / X / XE 后缀） |
| `bus` / `bus_clk` / `bus_speed` | 总线类型 / 频率 / 速率 |

### 内存

| 字段 | 说明 |
|---|---|
| `mem_type` | 支持类型，多值用 `;` 分隔，如 `DDR5-5600;DDR4-3200` |
| `mem_channels` | 通道数 |
| `mem_max` | 最大容量，GB |
| `mem_ecc` | `1` 支持 ECC |
| `mem_bandwidth` | 带宽，GB/s |

### PCIe

| 字段 | 说明 |
|---|---|
| `pcie_revision` | 版本，如 `5.0` |
| `pcie_lanes` | 通道总数 |
| `pcie_config` | 拆分方式，如 `x16, x4, x4` |

### 核显

| 字段 | 说明 |
|---|---|
| `graphics_name` | 核显名，无核显为 `null` |
| `graphics_clk` / `graphics_clk_boost` | 基础 / 加速频率，MHz |
| `graphics_core_config` | 执行单元配置，如 `32:0:0` 或 `12 CU` |

### 其它

| 字段 | 说明 |
|---|---|
| `instruction_set` | 指令集，逗号分隔 |
| `features` | 特性，逗号分隔 |
| `notes` | 备注 |
| `part_number` / `sspec` | 订货号 / Intel S-Spec |
| `data_width` | 数据位宽，通常 `64` |
| `image_cpu` / `image_author` | 图片索引 / 图片作者（`0` 表示无图） |
| `bm_cinebenchr15_single` / `bm_cinebenchr15_multi` | Cinebench R15 单核 / 多核 |
| `bm_geekbench4_single` / `bm_geekbench4_multi` | Geekbench 4 单核 / 多核 |
| `bm_passmark` | PassMark |

---

## 排序规则

界面上的顺序完全由三个字段决定：

1. `products.order_product` — 产品线在平台标签页内的顺序
2. `series.order_family` — 系列在产品线内的顺序
3. `cpu.order_number` — 型号在系列内的顺序

新增条目时只要把这三个值续接在原最大值之后，不需要改动任何代码。
