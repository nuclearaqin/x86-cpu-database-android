# -*- coding: utf-8 -*-
"""AMD server / embedded CPUs released between 2018-11 and 2026-11."""

from ds_common import C, S, ISA_AMD_ZEN, ISA_AMD_ZEN4, FEAT_AMD_SMT

AMD_SERVER = [

    # ------------------------------------------------------------ EPYC 7002 (Rome)
    S('amd', 25, 'EPYC 7002 Series', 2, dict(
        fab=7, arch='Zen 2', core_name='Rome', socket='SP3', pcie='4.0', lanes=128,
        pcie_cfg='x128, x64, x32, x16, x8', mem='DDR4-3200', ch=8, memmax=4096, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=2,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=204.8), [
        C('EPYC 7282', (2019, 8), 16, 32, 2800, 3200, 120, 65536, price=650.0),
        C('EPYC 7302', (2019, 8), 16, 32, 3000, 3300, 155, 131072, price=978.0),
        C('EPYC 7402', (2019, 8), 24, 48, 2800, 3350, 180, 131072, price=1783.0),
        C('EPYC 7502', (2019, 8), 32, 64, 2500, 3350, 180, 131072, price=2600.0),
        C('EPYC 7702', (2019, 8), 64, 128, 2000, 3350, 200, 262144, price=6450.0),
        C('EPYC 7702P', (2019, 8), 64, 128, 2000, 3350, 200, 262144, price=4425.0, multi=1),
        C('EPYC 7742', (2019, 8), 64, 128, 2250, 3400, 225, 262144, price=6950.0),
        C('EPYC 7H12', (2019, 9), 64, 128, 2600, 3300, 280, 262144, price=10000.0),
    ]),

    # ------------------------------------------------------------ EPYC 7003 (Milan)
    S('amd', 25, 'EPYC 7003 Series', 3, dict(
        fab=7, arch='Zen 3', core_name='Milan', socket='SP3', pcie='4.0', lanes=128,
        pcie_cfg='x128, x64, x32, x16, x8', mem='DDR4-3200', ch=8, memmax=4096, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=2,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=204.8), [
        C('EPYC 7313', (2021, 3), 16, 32, 3000, 3700, 155, 131072, price=1083.0),
        C('EPYC 7443', (2021, 3), 24, 48, 2850, 4000, 200, 131072, price=2010.0),
        C('EPYC 7543', (2021, 3), 32, 64, 2800, 3700, 225, 262144, price=3761.0),
        C('EPYC 7663', (2021, 3), 56, 112, 2000, 3500, 240, 262144, price=6366.0),
        C('EPYC 7713', (2021, 3), 64, 128, 2000, 3675, 225, 262144, price=7060.0),
        C('EPYC 7763', (2021, 3), 64, 128, 2450, 3500, 280, 262144, price=7890.0),
    ]),

    # ------------------------------------------------------------ EPYC 7004 (Milan-X)
    S('amd', 25, 'EPYC 7004 Series', 4, dict(
        fab=7, arch='Zen 3', core_name='Milan-X', socket='SP3', pcie='4.0', lanes=128,
        pcie_cfg='x128, x64, x32, x16, x8', mem='DDR4-3200', ch=8, memmax=4096, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=2,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=204.8), [
        C('EPYC 7373X', (2022, 3), 16, 32, 3050, 3800, 240, 786432, price=3416.0),
        C('EPYC 7473X', (2022, 3), 24, 48, 2800, 3700, 240, 786432, price=3901.0),
        C('EPYC 7573X', (2022, 3), 32, 64, 2800, 3600, 280, 786432, price=5590.0),
        C('EPYC 7773X', (2022, 3), 64, 128, 2200, 3500, 280, 786432, price=8800.0),
    ]),

    # ------------------------------------------------------------ EPYC 8004 (Siena)
    S('amd', 25, 'EPYC 8004 Series', 5, dict(
        fab=5, arch='Zen 4', core_name='Siena', socket='SP6', pcie='5.0', lanes=96,
        pcie_cfg='x96, x64, x32, x16, x8', mem='DDR5-4800', ch=6, memmax=1536, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=230.4), [
        C('EPYC 8224P', (2023, 9), 24, 48, 2550, 3000, 160, 65536, price=855.0),
        C('EPYC 8324P', (2023, 9), 32, 64, 2650, 3000, 180, 131072, price=1895.0),
        C('EPYC 8534P', (2023, 9), 64, 128, 2300, 3100, 200, 131072, price=4900.0),
    ]),

    # ------------------------------------------------------------ EPYC 9004 (Genoa / Bergamo / Genoa-X)
    S('amd', 25, 'EPYC 9004 Series', 6, dict(
        fab=5, arch='Zen 4', core_name='Genoa', socket='SP5', pcie='5.0', lanes=128,
        pcie_cfg='x128, x64, x32, x16, x8', mem='DDR5-4800', ch=12, memmax=6144, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=2,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=460.8), [
        C('EPYC 9174F', (2022, 11), 16, 32, 4100, 4400, 320, 262144, price=3850.0),
        C('EPYC 9254', (2022, 11), 24, 48, 2900, 4150, 200, 131072, price=2299.0),
        C('EPYC 9354', (2022, 11), 32, 64, 3250, 3800, 280, 262144, price=3420.0),
        C('EPYC 9454', (2022, 11), 48, 96, 2750, 3800, 290, 262144, price=5225.0),
        C('EPYC 9554', (2022, 11), 64, 128, 3100, 3750, 360, 262144, price=9087.0),
        C('EPYC 9654', (2022, 11), 96, 192, 2400, 3700, 360, 393216, price=11805.0),
        C('EPYC 9684X', (2023, 6), 96, 192, 2550, 3700, 400, 1179648, price=14756.0,
          core_name='Genoa-X'),
        C('EPYC 9734', (2023, 6), 112, 224, 2200, 3000, 340, 262144, price=9600.0,
          core_name='Bergamo', arch='Zen 4c'),
        C('EPYC 9754', (2023, 6), 128, 256, 2250, 3100, 360, 262144, price=11900.0,
          core_name='Bergamo', arch='Zen 4c'),
    ]),

    # ------------------------------------------------------------ EPYC 9005 (Turin)
    S('amd', 25, 'EPYC 9005 Series', 7, dict(
        fab=4, arch='Zen 5', core_name='Turin', socket='SP5', pcie='5.0', lanes=128,
        pcie_cfg='x128, x64, x32, x16, x8', mem='DDR5-6400', ch=12, memmax=6144, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=2,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=614.4), [
        C('EPYC 9175F', (2024, 10), 16, 32, 4000, 5000, 320, 524288, price=4256.0),
        C('EPYC 9355', (2024, 10), 32, 64, 3550, 4400, 280, 262144, price=3204.0),
        C('EPYC 9555', (2024, 10), 64, 128, 3200, 4400, 360, 393216, price=8981.0),
        C('EPYC 9655', (2024, 10), 96, 192, 2600, 4500, 400, 393216, price=11638.0),
        C('EPYC 9755', (2024, 10), 128, 256, 2700, 4100, 500, 524288, price=12984.0),
        C('EPYC 9965', (2024, 10), 192, 384, 2250, 3700, 500, 393216, price=14813.0,
          arch='Zen 5c'),
    ]),

    # ------------------------------------------------------------ EPYC Embedded 8004
    S('amd', 37, 'EPYC Embedded 8004 Series', 2, dict(
        fab=5, arch='Zen 4', core_name='Siena', socket='SP6', pcie='5.0', lanes=96,
        pcie_cfg='x96, x64, x32, x16', mem='DDR5-4800', ch=6, memmax=1536, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=230.4), [
        C('EPYC Embedded 8224P', (2023, 9), 24, 48, 2550, 3000, 160, 65536),
        C('EPYC Embedded 8534P', (2023, 9), 64, 128, 2300, 3100, 200, 131072),
    ]),

    # ------------------------------------------------------------ Ryzen Embedded V2000 / V3000
    S('amd', 36, 'Ryzen Embedded V2000 Series', 2, dict(
        fab=7, arch='Zen 2', core_name='Renoir', socket='FP6', pcie='3.0', lanes=20,
        pcie_cfg='x8, x4', mem='DDR4-3200;LPDDR4x-4266', ch=2, memmax=64, ecc=1,
        igpu='Radeon Graphics', igpu_clk=1600, igpu_boost=None, igpu_cfg='7 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=51.2), [
        C('Ryzen Embedded V2516', (2020, 11), 6, 12, 2100, 3950, 15, 8192),
        C('Ryzen Embedded V2718', (2020, 11), 8, 16, 1700, 4150, 15, 8192),
    ]),

    S('amd', 36, 'Ryzen Embedded V3000 Series', 3, dict(
        fab=6, arch='Zen 3+', core_name='Rembrandt', socket='FP7', pcie='4.0', lanes=20,
        pcie_cfg='x8, x4', mem='DDR5-4800', ch=2, memmax=64, ecc=1,
        igpu='Radeon Graphics', igpu_clk=2200, igpu_boost=None, igpu_cfg='12 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=76.8), [
        C('Ryzen Embedded V3C14', (2022, 9), 4, 8, 2300, 3800, 15, 8192),
        C('Ryzen Embedded V3C48', (2022, 9), 8, 16, 3300, 3800, 35, 16384),
    ]),
]
