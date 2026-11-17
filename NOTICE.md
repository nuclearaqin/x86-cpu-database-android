# 版权、来源与商标声明

## 原应用

本仓库的 Android 客户端（`dist/CPU-L-2.3.0-cpu2026.apk`）是对 **CPU-L 2.2.2** 的修改构建。

- 原始应用：CPU-L，作者 **iJR Software**，发布渠道 Google Play
- 包名：`com.ijsoft.cpul`
- 版权：Copyright © iJR Software

本项目**未获得**原作者的授权。修改内容包括：替换加密数据容器、提升数据版本号、调整部分界面尺寸资源。原应用的代码、界面设计、图标、数据库结构均归原作者所有。

APK 仅作**个人学习、技术研究与本地存档**用途，不作为对原作品的再授权，**不得用于商业目的或公开分发**。

如果权利人或其代理人认为本仓库内容不当，请在本仓库提交 issue，将立即删除相关内容。

## 数据集

`data/cpus_db.json` 的**字段结构与分类体系**源自 CPU-L 的数据库 schema，用于保证与原应用兼容。

其中的**规格数值**来自各厂商公开的技术资料：

- Intel ARK（ark.intel.com）与各代产品 Product Brief
- AMD 官方产品页与 Processor Specifications
- 厂商发布的 launch 新闻稿与规格表

这些属于公开事实性数据。本项目新增的 426 条记录由作者按上述来源整理，未复制任何第三方数据库的成段内容。

## 商标

Intel、Intel Core、Core Ultra、Xeon、Pentium、Celeron、Atom 是 Intel Corporation 的商标。
AMD、Ryzen、Threadripper、EPYC、Athlon 是 Advanced Micro Devices, Inc. 的商标。
Android、Google Play 是 Google LLC 的商标。

本项目与上述公司**无任何隶属、赞助或背书关系**。文中提及这些名称仅用于标识具体的产品型号，属描述性使用。

## 第三方组件

原应用打包了 SQLCipher、AppCompat、Firebase、AdMob、Crashlytics 等第三方库，其许可证随原包附带（`assets/open_source_licenses.html`）。本仓库不对这些组件做任何授权声明。

## 本仓库原创内容

`tools/` 下的脚本、`docs/` 下的文档，以及新增的 426 条 CPU 记录，由 **nuclearaqin** 编写，采用 MIT 许可证，详见 [LICENSE](LICENSE)。
