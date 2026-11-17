# x86 CPU 规格资料库（Android）

一个**离线**查阅历代 Intel / AMD 桌面、移动、服务器处理器规格的 Android 应用，内置 **4,350 款 CPU**、**4,862 条详情记录**，支持三级分类浏览、型号搜索、双型号对比、收藏与历史。

本仓库同时提供把这套数据**从加密容器解出、增量维护、重新打包签名**的完整可复现工具链。

> **当前版本：2.3.1**（2026-11-17）— 修复分类重复、启动卡顿、反复提示更新、排行榜型号错位、广告异常。详见 [docs/FIXES-2.3.1.md](docs/FIXES-2.3.1.md)。

---

> **免责声明**
> 本项目的 Android 客户端基于 iJR Software 的 *CPU-L* 2.2.2 进行**数据更新与界面适配**，仅作个人学习、技术研究与本地存档用途。原应用的代码、界面、图标及其整理的数据版权归原作者所有。仓库内的 APK 不构成对原作品的授权，**禁止任何商业使用或公开分发**。若权利人认为内容不当，请提 issue，会在第一时间删除。
> Intel、AMD、Core、Ryzen、EPYC、Xeon 等为各自公司的商标，本项目与上述公司无任何关联。

---

## 数据概览

| 维度 | 数量 |
|---|---:|
| CPU 型号总数 | **4,350**（Intel 2,894 / AMD 1,456） |
| 详情记录（含变体） | 4,862 |
| 系列 | 443 |
| 产品线 | 85（桌面 / 移动 / 服务器 / 嵌入式 / 定制 五类平台） |
| 单条详情字段 | 60 |
| 时间跨度 | 1993 – 2025 |

相比 2018-11 的原库（3,924 款）新增 **426 款**，覆盖 2019–2025 全部主流平台：

**Intel**
- 桌面：Core i3/i5/i7/i9 第 10–14 代、Core Ultra 5/7/9 Series 2（Arrow Lake-S）、Core i3 N 系列、Pentium Silver / Celeron N、Intel Processor N100–N250
- 移动：第 9 代 H、10 代（Ice Lake / Comet Lake）、11 代（Tiger Lake）、12 代（Alder Lake）、13 代（Raptor Lake）、14 代 HX、Core Ultra Series 1/2/2H（Meteor Lake / Lunar Lake / Arrow Lake-H）
- 服务器与工作站：Xeon Scalable 第 2–5 代、Xeon 6（Granite Rapids / Sierra Forest）、Xeon W-2200/2400/3300/3400、Xeon E-2200/2300/2400、Xeon D-2700、Atom x6000E

**AMD**
- 桌面：Ryzen 3000（Zen 2）/ 5000（Zen 3）/ 7000（Zen 4）/ 9000（Zen 5）、Ryzen 8000G、Threadripper 3000/7000/9000 及 PRO 系列、Athlon 3000G
- 移动：Ryzen 3000U/H、4000（Renoir）、5000（Cezanne）、6000（Rembrandt）、7000（Phoenix / Dragon Range）、8000（Hawk Point）、Ryzen AI 300 / AI Max 300
- 服务器：EPYC 7002（Rome）/ 7003（Milan）/ 7004（Milan-X）/ 8004（Siena）/ 9004（Genoa、Bergamo、Genoa-X）/ 9005（Turin）

---

## 目录结构

```
.
├── data/
│   └── cpus_db.json          明文数据集（7.1 MB，8 张表）
├── docs/
│   ├── FIXES-2.3.1.md        2.3.1 缺陷修复：分类重复、卡顿、误报更新、榜单错位
│   ├── CHANGELOG-2.3.0.md    2.3.0 改动的完整清单与验证结果
│   ├── data-pipeline.md      数据容器格式与解密/加密链路
│   └── schema.md             8 张表的字段定义与取值规范
├── tools/
│   ├── decrypt.py            从 assets/assets 解出 JSON
│   ├── ds_*.py               增量数据表（每个型号一行）
│   ├── build_data.py         合并进 8 张表、分配 id 与排序
│   ├── pack_data.py          JSON → ZIP → AES-256-CFB8
│   ├── patch_ui.py           界面尺寸/间距补丁
│   ├── validate.py           数据集结构与数值校验
│   └── check_apk.py          成品 APK 端到端校验
├── dist/
│   └── CPU-L-2.3.1-cpu2026.apk
├── LICENSE                   MIT，仅覆盖 tools/ 与 docs/ 原创内容
└── NOTICE.md                 版权、数据来源与商标声明
```

---

## 快速开始

### 只拿数据

`data/cpus_db.json` 就是全部内容，无需解密：

```python
import json
db = json.load(open('data/cpus_db.json', encoding='utf-8'))
print(db.keys())
# dict_keys(['amd_cpu','amd_cpu_data','amd_products','amd_series',
#            'intel_cpu','intel_cpu_data','intel_products','intel_series'])

for c in db['intel_cpu']:
    if c['name'] == 'Intel Core i9-14900K':
        print(c)
```

每条 `cpu` 通过 `id_serie` 挂到 `series`，`series` 通过 `id_product_family` 挂到 `products`；`cpu_data` 通过 `id_cpu` 关联，一个型号可有多条变体记录。

### 从原始 APK 复现数据

```bash
# 1. 解包
apktool d base.apk -o decoded

# 2. 解出数据容器
python tools/decrypt.py decoded/assets/assets cpus_db.zip

# 3. 重新构建数据集（含增量型号）
python tools/build_data.py

# 4. 回填数据容器
python tools/pack_data.py

# 5. 回编译
apktool b decoded -o unsigned.apk

# 6. 签名
uber-apk-signer --apks unsigned.apk --ks cpul.keystore --ksAlias cpul
```

### 追加新型号

在 `tools/ds_intel_*.py` 或 `tools/ds_amd_*.py` 对应系列里加一行：

```python
C('Core i5-14600K', (2023, 10), 14, 20, 3500, 5300, 125, 24576,
  igpu='UHD Graphics 770', unlock=1, price=319.0),
```

然后 `build_data.py` → `pack_data.py` → 重新打包。字段含义见 `docs/schema.md`。

---

## 实现要点

原应用把数据藏在一个加密容器里，链路为：

```
assets/assets (AES-256/CFB8)
  → 解密得到 ZIP
  → 解压得到 cpus_db（纯 JSON，非 SQLite）
  → 运行时由 JsonReader 逐字段导入 SQLCipher 本地库
```

密钥不写死在代码里，而是 `hex(MD5(包名))`，IV 由密钥反向隔位取样。细节见 `docs/data-pipeline.md`。

数据一致性上做了这些约束：

- 8 张表的**字段名、字段顺序、JSON 键序、字符串 / `null` 取值风格**与原库完全一致，原 3,924 条记录一条未改，全部尾部追加
- `order_number` 在每个系列内从 1 递增，`order_family` 续接原产品线最大序号
- L1 / L2 缓存沿用原库「总量」口径（Intel L1 = 32KB × 核数，L2 = 256KB × 核数；AMD Zen1–3 L1I 64KB、L1D 32KB，Zen4/5 均为 32KB）
- 无法确证的可选字段（`sspec`、`part_number`、`die_size`、`transistor_count`、跑分等）留 `null`，不臆造

---

## 覆盖边界

- **不含 2026 年新平台**：Intel Core Ultra Series 3（Panther Lake）、AMD Zen 6 在成稿时缺少可核验的公开规格表，为避免写入臆造数据未收录。数据集止于 2025 年已上市平台。
- **不含手机 SoC**：本项目只覆盖 x86 桌面 / 移动 / 服务器处理器，不含骁龙、天玑、Exynos 等 ARM 平台。
- 原库遗留的少量问题（个别 `cpu` 指向不存在的 `series`、3 组 AMD 同名记录、`AMD Ryzen Threadripper 1977X*` 无详情行）保持原样，避免影响既有条目。

---

## 许可

`tools/`、`docs/` 下由本项目编写的代码与文档采用 [MIT](LICENSE)。
`data/cpus_db.json` 的字段结构源自 CPU-L，规格数值来自各厂商公开的 product brief 与 ARK / 官方规格页。
`dist/` 下的 APK 为原应用的修改构建，**不在 MIT 授权范围内**，仅作存档，不得再分发。详见 [NOTICE.md](NOTICE.md)。
