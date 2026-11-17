# -*- coding: utf-8 -*-
"""Intel server / workstation / embedded CPUs, 2018-11 -> 2026-11."""

from ds_common import C, S, ISA_INTEL_9, ISA_INTEL_512, ISA_INTEL_ADL, FEAT_HT, FEAT_PLAIN

UPI = 'UPI'
PCIE_SRV = 'x16, x8, x4'


INTEL_SERVER = [

    # ------------------------------------------------------------ Xeon Scalable 2nd Gen (Cascade Lake)
    S('intel', 22, 'Xeon Scalable 2nd Generation', 35, dict(
        fab=14, arch='Cascade Lake', core_name='Cascade Lake-SP', socket='LGA3647',
        pcie='3.0', lanes=48, pcie_cfg='x48, x32, x16, x8, x4', mem='DDR4-2933', ch=6,
        memmax=1024, ecc=1, igpu=None, isa=ISA_INTEL_512, feat=FEAT_HT, bus=UPI,
        multi=2, mem_bw=140.8, tdp_multi=False,
    ), [
        C('Xeon Bronze 3204', (2019, 4), 6, 6, 1900, 1900, 85, 8448, price=213.0),
        C('Xeon Silver 4210', (2019, 4), 10, 20, 2200, 3200, 85, 14080, price=501.0),
        C('Xeon Gold 5218', (2019, 4), 16, 32, 2300, 3900, 125, 22528, price=1273.0),
        C('Xeon Gold 6230', (2019, 4), 20, 40, 2100, 3900, 125, 28160, price=1894.0),
        C('Xeon Gold 6248', (2019, 4), 20, 40, 2500, 3900, 150, 28160, price=3073.0),
        C('Xeon Gold 6252', (2019, 4), 24, 48, 2100, 3700, 150, 36608, price=3669.0),
        C('Xeon Platinum 8280', (2019, 4), 28, 56, 2700, 4000, 205, 39424, price=10009.0),
    ]),

    # ------------------------------------------------------------ Xeon Scalable 3rd Gen (Ice Lake-SP)
    S('intel', 22, 'Xeon Scalable 3rd Generation', 36, dict(
        fab=10, arch='Ice Lake', core_name='Ice Lake-SP', socket='LGA4189',
        pcie='4.0', lanes=64, pcie_cfg='x64, x32, x16, x8, x4', mem='DDR4-3200', ch=8,
        memmax=6144, ecc=1, igpu=None, isa=ISA_INTEL_512, feat=FEAT_HT, bus=UPI,
        multi=2, mem_bw=204.8,
    ), [
        C('Xeon Silver 4310', (2021, 4), 12, 24, 2100, 3300, 120, 18432, price=603.0),
        C('Xeon Gold 5318Y', (2021, 4), 24, 48, 2100, 3400, 165, 36864, price=1273.0),
        C('Xeon Gold 6338', (2021, 4), 32, 64, 2000, 3200, 205, 49152, price=2612.0),
        C('Xeon Gold 6348', (2021, 4), 28, 56, 2600, 3500, 235, 43008, price=3073.0),
        C('Xeon Platinum 8380', (2021, 4), 40, 80, 2300, 3400, 270, 61440, price=8099.0),
    ]),

    # ------------------------------------------------------------ Xeon Scalable 4th Gen (Sapphire Rapids)
    S('intel', 22, 'Xeon Scalable 4th Generation', 37, dict(
        fab=10, arch='Sapphire Rapids', core_name='Sapphire Rapids-SP', socket='LGA4677',
        pcie='5.0', lanes=80, pcie_cfg='x80, x64, x32, x16, x8, x4', mem='DDR5-4800', ch=8,
        memmax=6144, ecc=1, igpu=None, isa=ISA_INTEL_512, feat=FEAT_HT, bus=UPI,
        multi=2, mem_bw=307.2,
    ), [
        C('Xeon Silver 4410Y', (2023, 1), 12, 24, 2000, 3900, 150, 30720, price=563.0),
        C('Xeon Gold 6430', (2023, 1), 32, 64, 2100, 3400, 270, 61440, price=2139.0),
        C('Xeon Gold 6438Y+', (2023, 1), 32, 64, 2000, 4000, 205, 61440, price=2894.0),
        C('Xeon Platinum 8480+', (2023, 1), 56, 112, 2000, 3800, 350, 107520, price=10710.0),
    ]),

    # ------------------------------------------------------------ Xeon Scalable 5th Gen (Emerald Rapids)
    S('intel', 22, 'Xeon Scalable 5th Generation', 38, dict(
        fab=10, arch='Emerald Rapids', core_name='Emerald Rapids-SP', socket='LGA4677',
        pcie='5.0', lanes=80, pcie_cfg='x80, x64, x32, x16, x8, x4', mem='DDR5-5600', ch=8,
        memmax=6144, ecc=1, igpu=None, isa=ISA_INTEL_512, feat=FEAT_HT, bus=UPI,
        multi=2, mem_bw=358.4,
    ), [
        C('Xeon Gold 6530', (2023, 12), 32, 64, 2100, 4000, 270, 163840, price=2128.0),
        C('Xeon Gold 6548Y+', (2023, 12), 32, 64, 2500, 4100, 250, 61440, price=3726.0),
        C('Xeon Platinum 8592+', (2023, 12), 64, 128, 1900, 3900, 350, 327680, price=11600.0),
    ]),

    # ------------------------------------------------------------ Xeon 6 (Granite Rapids / Sierra Forest)
    S('intel', 22, 'Xeon 6', 39, dict(
        fab=3, arch='Redwood Cove', core_name='Granite Rapids-AP', socket='LGA7529',
        pcie='5.0', lanes=96, pcie_cfg='x96, x64, x32, x16', mem='DDR5-6400;MRDIMM-8800',
        ch=12, memmax=9216, ecc=1, igpu=None, isa=ISA_INTEL_512, feat=FEAT_HT, bus=UPI,
        multi=2, mem_bw=614.4,
    ), [
        C('Xeon 6980P', (2024, 9), 128, 256, 2000, 3900, 500, 516096, price=17800.0),
        C('Xeon 6979P', (2024, 9), 120, 240, 2100, 3900, 500, 504832, price=11100.0),
        C('Xeon 6780E', (2024, 6), 144, 144, 2200, 3000, 330, 110592,
          arch='Sierra Glen', core_name='Sierra Forest-SP', ch=8, mem='DDR5-6400',
          memmax=4096, lanes=88, mem_bw=409.6, price=11350.0),
    ]),

    # ------------------------------------------------------------ Xeon W 2200 (Cascade Lake-W)
    S('intel', 22, 'Xeon W 2200 Series', 40, dict(
        fab=14, arch='Cascade Lake', core_name='Cascade Lake-W', socket='LGA2066',
        pcie='3.0', lanes=48, pcie_cfg='x48, x32, x16, x8, x4', mem='DDR4-2933', ch=4,
        memmax=1024, ecc=1, igpu=None, isa=ISA_INTEL_512, feat=FEAT_HT, bus='DMI 3.0',
        multi=1, mem_bw=93.8,
    ), [
        C('Xeon W-2223', (2019, 10), 4, 8, 3600, 3900, 120, 8448, price=297.0),
        C('Xeon W-2245', (2019, 10), 8, 16, 3900, 4500, 155, 16896, price=1002.0),
        C('Xeon W-2265', (2019, 10), 12, 24, 3500, 4800, 165, 19712, price=1743.0),
        C('Xeon W-2275', (2019, 10), 14, 28, 3300, 4800, 165, 19712, price=2113.0),
        C('Xeon W-2295', (2019, 10), 18, 36, 3000, 4800, 165, 25344, price=2790.0),
    ]),

    # ------------------------------------------------------------ Xeon W 3300 (Ice Lake-W)
    S('intel', 22, 'Xeon W 3300 Series', 41, dict(
        fab=10, arch='Ice Lake', core_name='Ice Lake-W', socket='LGA4189',
        pcie='4.0', lanes=64, pcie_cfg='x64, x48, x32, x16', mem='DDR4-3200', ch=8,
        memmax=4096, ecc=1, igpu=None, isa=ISA_INTEL_512, feat=FEAT_HT, bus='DMI 3.0',
        multi=1, mem_bw=204.8,
    ), [
        C('Xeon W-3335', (2021, 7), 16, 32, 3400, 4000, 250, 24576, price=1296.0),
        C('Xeon W-3345', (2021, 7), 24, 48, 3000, 4000, 250, 36864, price=2499.0),
        C('Xeon W-3375', (2021, 7), 38, 76, 2500, 4000, 270, 58368, price=3500.0),
    ]),

    # ------------------------------------------------------------ Xeon W 3400 / 2400 (Sapphire Rapids WS)
    S('intel', 22, 'Xeon W 3400 Series', 42, dict(
        fab=10, arch='Sapphire Rapids', core_name='Sapphire Rapids-WS', socket='LGA4677',
        pcie='5.0', lanes=112, pcie_cfg='x112, x96, x64, x32, x16', mem='DDR5-4800', ch=8,
        memmax=4096, ecc=1, igpu=None, isa=ISA_INTEL_512, feat=FEAT_HT, bus='DMI 4.0',
        multi=1, mem_bw=307.2,
    ), [
        C('Xeon w5-3435X', (2023, 2), 16, 32, 3100, 4700, 270, 46080, price=1589.0, unlock=1),
        C('Xeon w7-3465X', (2023, 2), 28, 56, 2500, 4800, 300, 76800, price=2879.0, unlock=1),
        C('Xeon w9-3495X', (2023, 2), 56, 112, 1900, 4800, 350, 107520, price=5889.0,
          unlock=1),
    ]),

    S('intel', 22, 'Xeon W 2400 Series', 43, dict(
        fab=10, arch='Sapphire Rapids', core_name='Sapphire Rapids-WS', socket='LGA4677',
        pcie='5.0', lanes=64, pcie_cfg='x64, x48, x32, x16', mem='DDR5-4800', ch=4,
        memmax=2048, ecc=1, igpu=None, isa=ISA_INTEL_512, feat=FEAT_HT, bus='DMI 4.0',
        multi=1, mem_bw=153.6,
    ), [
        C('Xeon w5-2455X', (2023, 2), 12, 24, 3200, 4600, 200, 30720, price=1039.0, unlock=1),
        C('Xeon w7-2495X', (2023, 2), 24, 48, 2500, 4800, 225, 46080, price=2189.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Xeon E-2200 / E-2300 / E-2400
    S('intel', 22, 'Xeon E-2200 Series', 44, dict(
        fab=14, arch='Coffee Lake', core_name='Coffee Lake-S', socket='LGA1151',
        pcie='3.0', lanes=16, pcie_cfg='x16, x8, x4', mem='DDR4-2666', ch=2, memmax=128,
        ecc=1, igpu='UHD Graphics P630', igpu_clk=350, igpu_boost=1200, igpu_cfg='24:0:0',
        isa=ISA_INTEL_9, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=41.6,
    ), [
        C('Xeon E-2224', (2019, 5), 4, 4, 3400, 4600, 71, 8192, price=193.0, igpu=None),
        C('Xeon E-2246G', (2019, 5), 6, 12, 3600, 4800, 80, 12288, price=311.0),
        C('Xeon E-2288G', (2019, 5), 8, 16, 3700, 5000, 95, 16384, price=539.0),
    ]),

    S('intel', 22, 'Xeon E-2300 Series', 45, dict(
        fab=14, arch='Rocket Lake', core_name='Rocket Lake-S', socket='LGA1200',
        pcie='4.0', lanes=20, pcie_cfg='x16, x4', mem='DDR4-3200', ch=2, memmax=128,
        ecc=1, igpu='UHD Graphics P750', igpu_clk=350, igpu_boost=1300, igpu_cfg='32:0:0',
        isa=ISA_INTEL_512, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=51.2,
    ), [
        C('Xeon E-2314', (2021, 9), 4, 4, 2800, 4500, 65, 8192, price=182.0, igpu=None),
        C('Xeon E-2336', (2021, 9), 6, 12, 2900, 4800, 65, 12288, price=294.0),
        C('Xeon E-2388G', (2021, 9), 8, 16, 3200, 5100, 95, 16384, price=539.0),
    ]),

    S('intel', 22, 'Xeon E-2400 Series', 46, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-S', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg='x16, x4', mem='DDR5-4800', ch=2, memmax=128,
        ecc=1, igpu='UHD Graphics P770', igpu_clk=300, igpu_boost=1650, igpu_cfg='32:0:0',
        isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1, mem_bw=76.8,
    ), [
        C('Xeon E-2414', (2023, 12), 4, 4, 2600, 5200, 55, 6144, price=189.0, igpu=None),
        C('Xeon E-2436', (2023, 12), 6, 12, 2900, 5400, 65, 12288, price=302.0),
        C('Xeon E-2488', (2023, 12), 8, 16, 3200, 5600, 95, 16384, price=566.0),
    ]),

    # ------------------------------------------------------------ Xeon D-2700 (Ice Lake-D)
    S('intel', 22, 'Xeon D-2700 Series', 47, dict(
        fab=10, arch='Ice Lake', core_name='Ice Lake-D', socket='BGA2579',
        pcie='4.0', lanes=32, pcie_cfg='x32, x16, x8, x4', mem='DDR4-3200', ch=4,
        memmax=1024, ecc=1, igpu=None, isa=ISA_INTEL_512, feat=FEAT_HT, bus='UPI',
        multi=1, mem_bw=102.4,
    ), [
        C('Xeon D-2798NT', (2022, 2), 20, 40, 2100, 3100, 125, 30720, price=2283.0),
    ]),

    # ------------------------------------------------------------ Atom x6000E (Elkhart Lake, embedded)
    S('intel', 24, 'Atom x6000E Series', 4, dict(
        fab=10, arch='Tremont', core_name='Elkhart Lake', socket='BGA1493',
        pcie='3.0', lanes=8, pcie_cfg='x4, x2, x1', mem='DDR4-3200;LPDDR4x-4267', ch=2,
        memmax=32, ecc=1, igpu='UHD Graphics', igpu_clk=400, igpu_boost=850,
        igpu_cfg='32:0:0', isa='MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AES, EM64T',
        feat=FEAT_PLAIN, bus='DMI 3.0', multi=1, mem_bw=51.2,
    ), [
        C('Atom x6211E', (2021, 2), 2, 2, 1200, 3000, 10, 1536, price=102.0),
        C('Atom x6413E', (2021, 2), 4, 4, 1500, 3000, 10, 1536, price=131.0),
        C('Atom x6425E', (2021, 2), 4, 4, 1800, 3000, 12, 1536, price=167.0),
    ]),
]
