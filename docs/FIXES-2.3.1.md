# 2.3.1 缺陷修复说明

针对 2.3.0 反馈的 5 类问题逐项定位与修复。

| # | 反馈 | 根因 | 修复 |
|---|---|---|---|
| 1 | 分类不正确或重复 | 新增 `Pentium Silver` 系列与既有的同名系列（id 176）重复；移动端 `Core Ultra 5` 的 `order_product` 与 `Core i9` 撞号 | 数据层修正 |
| 2 | 打开软件没一会儿卡死 | 广告 SDK 在无 GMS 环境反复初始化 + 每进主页都发起数据库更新检查 | 广告全链路停用；更新检查短路 |
| 3 | 一直提示版本需要更新 | `MainActivity.onCreate` 内启动 `CheckUpdateMainDbAsync`，远端版本判断异常时每次进主页都弹框 | 检查任务返回 null 且回调判空 |
| 4 | 排行榜型号错误 | 排行榜读远端 `top_cpus.json` 写入的 `cpuTop` 表，其 `idCpu` 与本库对不上 | 改为本地库重建，型号与 id 一一对应 |
| 5 | 广告相关异常 | 同上，AdMob / Consent 依赖已失效的 GMS 与 AdMob 账号 | 同上 |

---

## 1. 分类重复与排序冲突

**`Pentium Silver` 重复**

原库在 `product 3`（Pentium / 桌面）下已有系列 id 176，2.3.0 又新建了一个同名系列（id 247）用于放 N6005，导致同一产品线下出现两个 `Pentium Silver`。

修复：`Pentium Silver N6005` 并入系列 176，`order_number` 续接为 2，删除重复系列。

```
修复前：176(1 款)  247(1 款)   ← product 3 下两个同名系列
修复后：176(2 款)              ← J5005, N6005
```

**`order_product` 撞号**

移动端产品线 `order_product` 已用到 12（`Core i9`），新增的 `Core Ultra 5/7/9` 也从 12 起，导致排序不稳定。

修复：改为 13 / 14 / 15。

**回归检查**

```
intel 系列重名        : none
intel 产品线排序冲突  : 仅剩 (dk,3) Atom/i860   ← 原库自带，未改动
amd  产品线排序冲突   : 仅剩 (mb,4) Athlon/Turion ← 原库自带，未改动
```

这两个残留冲突来自 2018 年原库，改动会影响既有条目的排序，故保持原样。

---

## 2 & 5. 广告与卡顿

`AdsHelper` 的 `a(Z)V` 是所有广告入口（主页、对比页、双型号对比页）的唯一入口，内部会：

1. 初始化 `ConsentInformation`（Google 用户同意 SDK）
2. 请求 GMS 更新同意状态
3. 回调中加载 AdMob 横幅

在无 GMS 或网络受限的设备上，第 1、2 步会反复重试并触发同意表单，是卡顿的主要来源。

修复：方法首行直接 `return-void`。

```smali
.method public final a(Z)V
    .locals 4
    return-void          # 后续代码不可达
    ...
```

副作用：横幅广告不再出现。`AdView` 在布局中本就是 `visibility="gone"`，代码不再改动它，因此不占位。

---

## 3. 反复提示版本更新

`CheckUpdateMainDbAsync`（`a/a`）在两处被启动：

| 位置 | 时机 |
|---|---|
| `SplashActivity` | 数据库就绪 + 有网络时 |
| `MainActivity.onCreate` | **每次进入主页** |

后者是"一直提示"的直接原因。远端 `db_cpus.json` 自 2018 年后未更新，但版本比较逻辑一旦得到异常值（网络劫持、返回空、解析失败），就会判定"有更新"并弹框。

修复：`a()` 直接返回 null，`onPostExecute` 判空跳过回调。

```smali
.method private varargs a()Lcom/ijsoft/cpul/c/q;
    const/4 v0, 0x0
    return-object v0
```

```smali
check-cast p1, Lcom/ijsoft/cpul/c/q;
if-eqz p1, :done      # 无更新时不回调，避免空指针
```

一处修改同时覆盖 Splash 与 MainActivity，且不再发起任何网络请求。

---

## 4. 排行榜型号错误

`TopCpuFragment` 读取 `db_user.cpuTop` 表（字段 `idCpu` / `idBrand` / `nameCpu`）。该表由 `CheckUpdateTopListAsync` 从 `ijrsoftware.com/json/top_cpus.json` 下载后写入。

远端列表与本地库的 id 体系不一致，表现为：榜单上显示 A 型号，点进去却是 B，或提示 `CPU not available in this version / Please update the application`（这也是用户感知到的"提示版本需要更新"之一）。

修复：主库导入完成后，用本地数据重建榜单。

```smali
# d/g->a(Z I Context) 导入成功分支内
invoke-static {p2, v6}, Lcom/ijsoft/cpul/d/g;->rebuildTopList(Landroid/content/Context;Lnet/sqlcipher/database/SQLiteDatabase;)V
```

```smali
.method public static rebuildTopList(Landroid/content/Context;Lnet/sqlcipher/database/SQLiteDatabase;)V
    # 复用现有的 d/g->a(I, Context, SQLiteDatabase)
    #   参数 1 = Intel，0 = AMD；内部按 launch DESC, _id DESC 取前 50
    # 合并后用 d/i->a(ArrayList, Context) 写入 cpuTop（先 delete 全表再批量 insert）
```

写入方法 `d/i->a(ArrayList, Context)` 会先 `delete("cpuTop")` 再事务插入，因此旧的错误记录被彻底清除。

结果：榜单为 Intel 50 + AMD 50 共 100 款最新处理器，型号、id、品牌三者一致，点击必然可查。

语义变化：从"远端热门榜"变为"本地最新榜"。在远端服务已停更 8 年的前提下，这是唯一能保证数据正确的方案。

---

## 版本与升级

| 项 | 2.3.0 | 2.3.1 |
|---|---|---|
| versionCode | 202611 | **202612** |
| versionName | 2.3.0 | **2.3.1** |
| 内置数据库版本 | 0xC0B0B11 | **0xC0B0B12** |
| 系列数 | 444 | 443（删除重复） |

数据库版本提升后，**已装 2.3.0 的设备覆盖安装会重新导入一次数据**（约数秒，仅此一次），分类修正与榜单重建随之生效。

---

## 验证

| 检查项 | 结果 |
|---|---|
| apktool 回编译 | 通过 |
| 签名 | v1 + v2 + v3 通过 |
| 成品回解 | versionCode 202612 / versionName 2.3.1 / minSdk 16 / targetSdk 28 |
| 数据完整性 | 4,350 型号 / 4,862 详情 / 443 系列 / 85 产品线 |
| 建表 + 全量插入模拟 | 9,741 行全部成功，无类型错误 |
| 字段类型与原库一致性 | 偏差 0 |
| dex 内改动确认 | 三处均已在成品中反编译验证 |
| 主线程网络调用 | 无（均已确认在 AsyncTask 内） |

---

## 仍未解决

**未在真机验证**。以上结论基于静态分析 + 数据模拟，无法覆盖设备侧的运行时行为。若安装 2.3.1 后仍卡顿，需要 `logcat` 抓取 ANR 堆栈才能定位：

```bash
adb logcat -b main,crash -v time | findstr /i "cpul ANR Fatal"
```

另外，`errCPUnotAvailable` 提示还有一条独立路径：收藏或历史里保存了旧版数据库的 CPU id。重建后未清理这两张表，若仍有该提示，可清除应用数据后重新收藏。
