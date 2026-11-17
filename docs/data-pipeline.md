# 数据容器与加解密链路

本文记录 CPU-L 2.2.2 的数据承载方式，以及本项目为更新数据所做的复现步骤。目的是让数据可以被审计、被增量维护，而不是黑盒。

## 应用基本信息

| 项 | 值 |
|---|---|
| 包名 | `com.ijsoft.cpul` |
| 版本 | 2.2.2 / versionCode 202020（原始） |
| minSdk / targetSdk | 16 / 28 |
| 架构 | 单 dex，`libsqlcipher.so`（arm64-v8a、armeabi、armeabi-v7a、x86、x86_64） |
| 本地库 | SQLCipher，库名 `cpus`，口令即数据容器密钥 |

## 数据容器的三层结构

```
assets/assets            350,456 B，高熵二进制，无文件头
   │  AES-256 / CFB8 / NoPadding 解密（原地流式）
   ▼
ZIP（仅一个条目）
   │  ZipInputStream 取首个 entry → filesDir/tmp_uz
   ▼
cpus_db                  6.4 MB，纯 JSON
   │  JsonReader 逐字段解析
   ▼
SQLCipher `cpus` 库，8 张表
```

注意两点：

1. 解密后的内容是 **ZIP**，不是数据库文件。解开 ZIP 得到的 `cpus_db` 也不是 SQLite，而是 JSON —— 文件名有误导性。
2. 应用每次冷启动若判定需要导入，都会重新走「解密 → 解压 → 逐行 INSERT」这条链，所以容器体积直接决定首启耗时。

## 密钥派生

密钥没有硬编码，而是从包名派生：

```java
// d/f.java  c(Context)
byte[] seed = context.getPackageName().getBytes();      // "com.ijsoft.cpul"
String key  = md5Hex(seed);                              // 32 字符 ASCII
byte[] iv   = new byte[16];
for (int i = 0; i < 32; i += 2) iv[i / 2] = keyBytes[31 - i];
Cipher c = Cipher.getInstance("AES/CFB8/NoPadding");
c.init(DECRYPT_MODE, new SecretKeySpec(keyBytes, "AES"), new IvParameterSpec(iv));
```

- 摘要算法名来自字符串资源 `hash`（`0x7f0f00cb`），值为 `MD5`
- 密钥是 **32 字节的十六进制字符串本身**，即 AES-256
- IV 是密钥字节的**反向隔位取样**：`key[31], key[29], …, key[1]`
- CFB8 是流模式，密文与明文等长，无填充，可边读边写

对 `com.ijsoft.cpul` 派生结果：

```
key = 4819cb0ccc29370ab10c29c5ed289b90
iv  = 30 62 38 64 35 39 63 31 61 37 39 63 63 62 39 38
```

因为密钥绑定包名，**修改包名必须同步重新加密容器**，否则解密出乱码、导入失败。

## 参考实现

最小解密（见 `tools/decrypt.py`）：

```python
import hashlib
from Crypto.Cipher import AES

PKG = 'com.ijsoft.cpul'
key = hashlib.md5(PKG.encode()).hexdigest().encode()
iv  = bytes(key[31 - 2 * i] for i in range(16))
plain = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=8).decrypt(blob)
```

反向打包（见 `tools/pack_data.py`）：JSON → 单条目 ZIP（deflate 9）→ 同参数加密。必须满足：

- ZIP 内**只有一个条目**，应用只读第一个 entry，不看名字
- 输出长度与 ZIP 相同（CFB8 无填充）
- APK 内 `assets/assets` 需保持**不压缩存储**（`apktool.yml` 的 `doNotCompress`），与原包一致

## 导入逻辑位置

| 环节 | 文件 | 说明 |
|---|---|---|
| 解密 | `smali/com/ijsoft/cpul/d/a.smali` | `AES256Cipher`，写 `tmp_dc` |
| 密钥派生 | `smali/com/ijsoft/cpul/d/f.smali` | `c(Context)`、`a([B, Context)` |
| 解压 | `smali/com/ijsoft/cpul/d/m.smali` | `ZipUtils`，写 `tmp_uz` |
| 建表 | `smali/com/ijsoft/cpul/d/h.smali` | 8 张表 CREATE TABLE |
| 导入 | `smali/com/ijsoft/cpul/d/g.smali` | `JsonReader` 逐字段入库，事务包裹 |
| 模型 | `smali/com/ijsoft/cpul/c/j.smali` | `DbCpu`，60 字段映射 |

## 版本号与远端库

内置数据版本是一个整型常量 `0xC0764D9`，出现在 5 处：

- `SplashActivity.smali`（2 处）
- `SplashActivity$a.smali`（1 处）
- `a/a.smali`（2 处）

判断逻辑是 `内置版本 > SharedPreferences["release_main_db"]` 时执行导入，并把当前版本写回。导入完成后收藏、历史等用户数据存放在同一 SQLCipher 库的 `cpuFavorite` / `cpuHistory` / `cpuTop` 表中。

应用还会请求 `ijrsoftware.com/json/db_cpus.json` 做在线更新，比较远端版本与 `max(本地版本, 内置版本)`。

**抬高内置版本常量有两个作用**：

1. 老用户升级后自动重新导入新数据；
2. 远端仍是 2018 年的库，版本低于内置值，不会把新数据覆盖掉。

若清空应用数据，`release_main_db` 归零，下次启动同样会重新导入。

## 签名与覆盖安装

原包使用发布者私钥签名，无法复用。本项目的重建包使用独立密钥，因此：

- 覆盖安装会报签名冲突，**必须先卸载旧版**；
- 卸载会清除收藏与浏览历史；
- 后续版本请沿用同一密钥，否则同样需要卸载重装。

## 首启耗时

容器内含 7.0 MB JSON / 4,350 条型号，需在设备上完成「解密 → 解压 → 4,862 次 INSERT」。实测较原包首启增加数秒，属预期行为；导入完成后不再重复。
