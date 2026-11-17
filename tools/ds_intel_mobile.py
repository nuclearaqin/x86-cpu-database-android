# -*- coding: utf-8 -*-
"""Intel mobile / low-power CPUs released between 2018-11 and 2026-11."""

from ds_common import (C, S, ISA_INTEL_9, ISA_INTEL_512, ISA_INTEL_ADL, ISA_INTEL_ARL,
                       FEAT_HT, FEAT_HT_NOVT, FEAT_PLAIN, FEAT_PLAIN2, PCIE_CFG16,
                       PCIE_CFG20)

INTEL_MOBILE = [

    # ------------------------------------------------------------ Core i5 9th (Coffee Lake-HR)
    S('intel', 17, 'Core i5 9th Generation', 9, dict(
        fab=14, arch='Coffee Lake', core_name='Coffee Lake-HR', socket='BGA1440',
        pcie='3.0', lanes=16, pcie_cfg=PCIE_CFG16, mem='DDR4-2666', ch=2, memmax=128, ecc=0,
        igpu='UHD Graphics 630', igpu_clk=350, igpu_boost=1050, igpu_cfg='24:0:0',
        isa=ISA_INTEL_9, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=41.6), [
        C('Core i5-9300H', (2019, 4), 4, 8, 2400, 4100, 45, 8192, price=250.0),
        C('Core i5-9300HF', (2019, 4), 4, 8, 2400, 4100, 45, 8192, price=250.0, igpu=None),
    ]),

    # ------------------------------------------------------------ Core i7 9th (Coffee Lake-HR)
    S('intel', 18, 'Core i7 9th Generation', 9, dict(
        fab=14, arch='Coffee Lake', core_name='Coffee Lake-HR', socket='BGA1440',
        pcie='3.0', lanes=16, pcie_cfg=PCIE_CFG16, mem='DDR4-2666', ch=2, memmax=128, ecc=0,
        igpu='UHD Graphics 630', igpu_clk=350, igpu_boost=1150, igpu_cfg='24:0:0',
        isa=ISA_INTEL_9, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=41.6), [
        C('Core i7-9750H', (2019, 4), 6, 12, 2600, 4500, 45, 12288, price=395.0),
        C('Core i7-9750HF', (2019, 4), 6, 12, 2600, 4500, 45, 12288, price=395.0, igpu=None),
        C('Core i7-9850H', (2019, 4), 6, 12, 2600, 4600, 45, 12288, price=556.0),
    ]),

    # ------------------------------------------------------------ Core i9 9th (Coffee Lake-HR)
    S('intel', 37, 'Core i9 9th Generation', 2, dict(
        fab=14, arch='Coffee Lake', core_name='Coffee Lake-HR', socket='BGA1440',
        pcie='3.0', lanes=16, pcie_cfg=PCIE_CFG16, mem='DDR4-2666', ch=2, memmax=128, ecc=0,
        igpu='UHD Graphics 630', igpu_clk=350, igpu_boost=1250, igpu_cfg='24:0:0',
        isa=ISA_INTEL_9, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=41.6), [
        C('Core i9-9880H', (2019, 4), 8, 16, 2300, 4800, 45, 16384, price=556.0),
        C('Core i9-9980HK', (2019, 4), 8, 16, 2400, 5000, 45, 16384, price=583.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i3 10th (Ice Lake-U / Comet Lake-U)
    S('intel', 16, 'Core i3 10th Generation', 9, dict(
        fab=10, arch='Ice Lake', core_name='Ice Lake-U', socket='BGA1526',
        pcie='3.0', lanes=16, pcie_cfg=PCIE_CFG16, mem='DDR4-3200;LPDDR4-3733', ch=2,
        memmax=64, ecc=0, igpu='UHD Graphics G4', igpu_clk=300, igpu_boost=1050,
        igpu_cfg='32:0:0', isa=ISA_INTEL_512, feat=FEAT_HT_NOVT, bus='OPI', multi=1,
        mem_bw=59.7), [
        C('Core i3-1005G1', (2019, 8), 2, 4, 1200, 3400, 15, 4096, price=281.0),
        C('Core i3-10110U', (2019, 8), 2, 4, 2100, 4100, 15, 4096, price=281.0,
          fab=14, arch='Comet Lake', core_name='Comet Lake-U', socket='BGA1528',
          igpu='UHD Graphics 620', isa=ISA_INTEL_9),
    ]),

    # ------------------------------------------------------------ Core i5 10th (Ice Lake-U / Comet Lake-U / H)
    S('intel', 17, 'Core i5 10th Generation', 10, dict(
        fab=10, arch='Ice Lake', core_name='Ice Lake-U', socket='BGA1526',
        pcie='3.0', lanes=16, pcie_cfg=PCIE_CFG16, mem='DDR4-3200;LPDDR4-3733', ch=2,
        memmax=64, ecc=0, igpu='UHD Graphics G1', igpu_clk=300, igpu_boost=1050,
        igpu_cfg='32:0:0', isa=ISA_INTEL_512, feat=FEAT_HT_NOVT, bus='OPI', multi=1,
        mem_bw=59.7), [
        C('Core i5-10210U', (2019, 8), 4, 8, 1600, 4200, 15, 6144, price=297.0,
          fab=14, arch='Comet Lake', core_name='Comet Lake-U', socket='BGA1528',
          igpu='UHD Graphics 620', isa=ISA_INTEL_9),
        C('Core i5-1035G1', (2019, 8), 4, 8, 1000, 3600, 15, 6144, price=297.0),
        C('Core i5-1035G4', (2019, 8), 4, 8, 1100, 3700, 15, 6144, price=309.0,
          igpu='Iris Plus Graphics G4', igpu_cfg='48:0:0'),
        C('Core i5-1035G7', (2019, 8), 4, 8, 1200, 3700, 15, 6144, price=320.0,
          igpu='Iris Plus Graphics G7', igpu_cfg='64:0:0'),
        C('Core i5-10300H', (2020, 4), 4, 8, 2500, 4500, 45, 8192, price=250.0,
          fab=14, arch='Comet Lake', core_name='Comet Lake-H', socket='BGA1440',
          igpu='UHD Graphics 630', isa=ISA_INTEL_9, bus='DMI 3.0', mem='DDR4-2933',
          memmax=128, mem_bw=45.8),
        C('Core i5-10400H', (2020, 4), 4, 8, 2600, 4600, 45, 8192, price=250.0,
          fab=14, arch='Comet Lake', core_name='Comet Lake-H', socket='BGA1440',
          igpu='UHD Graphics 630', isa=ISA_INTEL_9, bus='DMI 3.0', mem='DDR4-2933',
          memmax=128, mem_bw=45.8),
        C('Core i5-10500H', (2020, 8), 6, 12, 2500, 4500, 45, 12288,
          fab=14, arch='Comet Lake', core_name='Comet Lake-H', socket='BGA1440',
          igpu='UHD Graphics 630', isa=ISA_INTEL_9, bus='DMI 3.0', mem='DDR4-2933',
          memmax=128, mem_bw=45.8),
    ]),

    # ------------------------------------------------------------ Core i7 10th (Ice Lake-U / Comet Lake-U / H)
    S('intel', 18, 'Core i7 10th Generation', 10, dict(
        fab=10, arch='Ice Lake', core_name='Ice Lake-U', socket='BGA1526',
        pcie='3.0', lanes=16, pcie_cfg=PCIE_CFG16, mem='DDR4-3200;LPDDR4-3733', ch=2,
        memmax=64, ecc=0, igpu='Iris Plus Graphics G7', igpu_clk=300, igpu_boost=1100,
        igpu_cfg='64:0:0', isa=ISA_INTEL_512, feat=FEAT_HT_NOVT, bus='OPI', multi=1,
        mem_bw=59.7), [
        C('Core i7-10510U', (2019, 8), 4, 8, 1800, 4900, 15, 8192, price=409.0,
          fab=14, arch='Comet Lake', core_name='Comet Lake-U', socket='BGA1528',
          igpu='UHD Graphics 620', isa=ISA_INTEL_9),
        C('Core i7-1065G7', (2019, 8), 4, 8, 1300, 3900, 15, 8192, price=426.0),
        C('Core i7-10610U', (2020, 4), 4, 8, 1800, 4900, 15, 8192,
          fab=14, arch='Comet Lake', core_name='Comet Lake-U', socket='BGA1528',
          igpu='UHD Graphics 620', isa=ISA_INTEL_9),
        C('Core i7-10710U', (2019, 8), 6, 12, 1100, 4700, 15, 12288, price=443.0,
          fab=14, arch='Comet Lake', core_name='Comet Lake-U', socket='BGA1528',
          igpu='UHD Graphics 620', isa=ISA_INTEL_9),
        C('Core i7-10750H', (2020, 4), 6, 12, 2600, 5000, 45, 12288, price=395.0,
          fab=14, arch='Comet Lake', core_name='Comet Lake-H', socket='BGA1440',
          igpu='UHD Graphics 630', isa=ISA_INTEL_9, bus='DMI 3.0', mem='DDR4-2933',
          memmax=128, mem_bw=45.8),
        C('Core i7-10850H', (2020, 4), 6, 12, 2700, 5100, 45, 12288, price=443.0,
          fab=14, arch='Comet Lake', core_name='Comet Lake-H', socket='BGA1440',
          igpu='UHD Graphics 630', isa=ISA_INTEL_9, bus='DMI 3.0', mem='DDR4-2933',
          memmax=128, mem_bw=45.8, unlock=1),
        C('Core i7-10875H', (2020, 4), 8, 16, 2300, 5100, 45, 16384, price=450.0,
          fab=14, arch='Comet Lake', core_name='Comet Lake-H', socket='BGA1440',
          igpu='UHD Graphics 630', isa=ISA_INTEL_9, bus='DMI 3.0', mem='DDR4-2933',
          memmax=128, mem_bw=45.8),
    ]),

    # ------------------------------------------------------------ Core i9 10th (Comet Lake-H)
    S('intel', 37, 'Core i9 10th Generation', 3, dict(
        fab=14, arch='Comet Lake', core_name='Comet Lake-H', socket='BGA1440',
        pcie='3.0', lanes=16, pcie_cfg=PCIE_CFG16, mem='DDR4-2933', ch=2, memmax=128,
        ecc=0, igpu='UHD Graphics 630', igpu_clk=350, igpu_boost=1250, igpu_cfg='24:0:0',
        isa=ISA_INTEL_9, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=45.8), [
        C('Core i9-10885H', (2020, 4), 8, 16, 2400, 5300, 45, 16384, price=556.0, unlock=1),
        C('Core i9-10980HK', (2020, 4), 8, 16, 2400, 5300, 45, 16384, price=583.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i3 11th (Tiger Lake-UP3)
    S('intel', 16, 'Core i3 11th Generation', 10, dict(
        fab=10, arch='Tiger Lake', core_name='Tiger Lake-UP3', socket='BGA1449',
        pcie='4.0', lanes=16, pcie_cfg='x4, x1', mem='DDR4-3200;LPDDR4x-4266', ch=2,
        memmax=64, ecc=0, igpu='UHD Graphics G4', igpu_clk=300, igpu_boost=1250,
        igpu_cfg='48:0:0', isa=ISA_INTEL_512, feat=FEAT_HT_NOVT, bus='OPI', multi=1,
        mem_bw=68.3), [
        C('Core i3-1115G4', (2020, 9), 2, 4, 3000, 4100, 15, 6144, price=281.0),
        C('Core i3-1125G4', (2021, 1), 4, 8, 2000, 3700, 15, 8192, price=281.0),
    ]),

    # ------------------------------------------------------------ Core i5 11th (Tiger Lake-UP3 / H)
    S('intel', 17, 'Core i5 11th Generation', 11, dict(
        fab=10, arch='Tiger Lake', core_name='Tiger Lake-UP3', socket='BGA1449',
        pcie='4.0', lanes=16, pcie_cfg='x4, x1', mem='DDR4-3200;LPDDR4x-4266', ch=2,
        memmax=64, ecc=0, igpu='Iris Xe Graphics G7', igpu_clk=400, igpu_boost=1300,
        igpu_cfg='80:0:0', isa=ISA_INTEL_512, feat=FEAT_HT_NOVT, bus='OPI', multi=1,
        mem_bw=68.3), [
        C('Core i5-1135G7', (2020, 9), 4, 8, 2400, 4200, 15, 8192, price=309.0),
        C('Core i5-1145G7', (2020, 9), 4, 8, 2600, 4400, 15, 8192, price=309.0),
        C('Core i5-11300H', (2021, 1), 4, 8, 3100, 4400, 35, 8192, price=309.0),
        C('Core i5-11400H', (2021, 5), 6, 12, 2700, 4500, 45, 12288, price=250.0,
          core_name='Tiger Lake-H', socket='BGA1787', lanes=20, pcie_cfg='x16, x4, x1',
          mem='DDR4-3200', igpu_boost=1450),
        C('Core i5-11500H', (2021, 5), 6, 12, 2900, 4600, 45, 12288, price=250.0,
          core_name='Tiger Lake-H', socket='BGA1787', lanes=20, pcie_cfg='x16, x4, x1',
          mem='DDR4-3200', igpu_boost=1450),
    ]),

    # ------------------------------------------------------------ Core i7 11th (Tiger Lake-UP3 / H)
    S('intel', 18, 'Core i7 11th Generation', 11, dict(
        fab=10, arch='Tiger Lake', core_name='Tiger Lake-UP3', socket='BGA1449',
        pcie='4.0', lanes=16, pcie_cfg='x4, x1', mem='DDR4-3200;LPDDR4x-4266', ch=2,
        memmax=64, ecc=0, igpu='Iris Xe Graphics G7', igpu_clk=400, igpu_boost=1300,
        igpu_cfg='96:0:0', isa=ISA_INTEL_512, feat=FEAT_HT_NOVT, bus='OPI', multi=1,
        mem_bw=68.3), [
        C('Core i7-1165G7', (2020, 9), 4, 8, 2800, 4700, 15, 12288, price=426.0),
        C('Core i7-1185G7', (2020, 9), 4, 8, 3000, 4800, 15, 12288, price=426.0),
        C('Core i7-1195G7', (2021, 6), 4, 8, 2900, 5000, 15, 12288, price=426.0),
        C('Core i7-11370H', (2021, 1), 4, 8, 3300, 4800, 35, 12288, price=426.0),
        C('Core i7-11375H', (2021, 1), 4, 8, 3300, 5000, 35, 12288, price=482.0),
        C('Core i7-11800H', (2021, 5), 8, 16, 2300, 4600, 45, 24576, price=395.0,
          core_name='Tiger Lake-H', socket='BGA1787', lanes=20, pcie_cfg='x16, x4, x1',
          mem='DDR4-3200', igpu_boost=1450),
    ]),

    # ------------------------------------------------------------ Core i9 11th (Tiger Lake-H)
    S('intel', 37, 'Core i9 11th Generation', 4, dict(
        fab=10, arch='Tiger Lake', core_name='Tiger Lake-H', socket='BGA1787',
        pcie='4.0', lanes=20, pcie_cfg='x16, x4, x1', mem='DDR4-3200', ch=2, memmax=128,
        ecc=0, igpu='Iris Xe Graphics G7', igpu_clk=350, igpu_boost=1450, igpu_cfg='96:0:0',
        isa=ISA_INTEL_512, feat=FEAT_HT_NOVT, bus='DMI 3.0', multi=1, mem_bw=51.2), [
        C('Core i9-11900H', (2021, 5), 8, 16, 2500, 4900, 45, 24576, price=546.0),
        C('Core i9-11950H', (2021, 5), 8, 16, 2600, 5000, 45, 24576, price=556.0),
        C('Core i9-11980HK', (2021, 5), 8, 16, 2600, 5000, 65, 24576, price=583.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i3 12th (Alder Lake-U/P)
    S('intel', 16, 'Core i3 12th Generation', 11, dict(
        fab=10, arch='Alder Lake', core_name='Alder Lake-U', socket='BGA1744',
        pcie='4.0', lanes=20, pcie_cfg='x4, x1', mem='DDR5-4800;DDR4-3200;LPDDR5-5200',
        ch=2, memmax=64, ecc=0, igpu='UHD Graphics', igpu_clk=300, igpu_boost=1250,
        igpu_cfg='64:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='OPI', multi=1,
        mem_bw=76.8), [
        C('Core i3-1215U', (2022, 2), 6, 8, 1200, 4400, 15, 10240, price=309.0),
        C('Core i3-1220P', (2022, 2), 10, 12, 1500, 4400, 28, 12288, price=309.0,
          core_name='Alder Lake-P', igpu_boost=1100),
    ]),

    # ------------------------------------------------------------ Core i5 12th (Alder Lake-U/P/H)
    S('intel', 17, 'Core i5 12th Generation', 12, dict(
        fab=10, arch='Alder Lake', core_name='Alder Lake-U', socket='BGA1744',
        pcie='4.0', lanes=20, pcie_cfg='x4, x1', mem='DDR5-4800;DDR4-3200;LPDDR5-5200',
        ch=2, memmax=64, ecc=0, igpu='Iris Xe Graphics G7', igpu_clk=300, igpu_boost=1200,
        igpu_cfg='80:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='OPI', multi=1,
        mem_bw=76.8), [
        C('Core i5-1235U', (2022, 2), 10, 12, 1300, 4400, 15, 12288, price=309.0),
        C('Core i5-1240P', (2022, 2), 12, 16, 1700, 4400, 28, 12288, price=320.0,
          core_name='Alder Lake-P', igpu_boost=1300),
        C('Core i5-12450H', (2022, 2), 8, 12, 2000, 4400, 45, 12288, price=311.0,
          core_name='Alder Lake-H', socket='BGA1744', lanes=28, pcie_cfg='x16, x4, x8',
          memmax=128, igpu_boost=1200),
        C('Core i5-12500H', (2022, 2), 12, 16, 2500, 4500, 45, 18432, price=311.0,
          core_name='Alder Lake-H', socket='BGA1744', lanes=28, pcie_cfg='x16, x4, x8',
          memmax=128, igpu_boost=1300),
    ]),

    # ------------------------------------------------------------ Core i7 12th (Alder Lake-U/P/H)
    S('intel', 18, 'Core i7 12th Generation', 12, dict(
        fab=10, arch='Alder Lake', core_name='Alder Lake-U', socket='BGA1744',
        pcie='4.0', lanes=20, pcie_cfg='x4, x1', mem='DDR5-4800;DDR4-3200;LPDDR5-5200',
        ch=2, memmax=64, ecc=0, igpu='Iris Xe Graphics G7', igpu_clk=300, igpu_boost=1250,
        igpu_cfg='96:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='OPI', multi=1,
        mem_bw=76.8), [
        C('Core i7-1255U', (2022, 2), 10, 12, 1700, 4700, 15, 12288, price=469.0),
        C('Core i7-1260P', (2022, 2), 12, 16, 2100, 4700, 28, 18432, price=480.0,
          core_name='Alder Lake-P', igpu_boost=1400),
        C('Core i7-1280P', (2022, 2), 14, 20, 1800, 4800, 28, 24576, price=482.0,
          core_name='Alder Lake-P', igpu_boost=1450),
        C('Core i7-12650H', (2022, 2), 10, 16, 2300, 4700, 45, 24576, price=457.0,
          core_name='Alder Lake-H', lanes=28, pcie_cfg='x16, x4, x8', memmax=128,
          igpu_boost=1400),
        C('Core i7-12700H', (2022, 2), 14, 20, 2300, 4700, 45, 24576, price=502.0,
          core_name='Alder Lake-H', lanes=28, pcie_cfg='x16, x4, x8', memmax=128,
          igpu_boost=1400),
    ]),

    # ------------------------------------------------------------ Core i9 12th (Alder Lake-H/HX)
    S('intel', 37, 'Core i9 12th Generation', 5, dict(
        fab=10, arch='Alder Lake', core_name='Alder Lake-H', socket='BGA1744',
        pcie='5.0', lanes=28, pcie_cfg='x16, x4, x8', mem='DDR5-4800;DDR4-3200', ch=2,
        memmax=128, ecc=0, igpu='Iris Xe Graphics G7', igpu_clk=350, igpu_boost=1450,
        igpu_cfg='96:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=76.8), [
        C('Core i9-12900H', (2022, 2), 14, 20, 2500, 5000, 45, 24576, price=617.0),
        C('Core i9-12900HK', (2022, 2), 14, 20, 2500, 5000, 45, 24576, price=697.0, unlock=1),
        C('Core i9-12950HX', (2022, 5), 16, 24, 2300, 5000, 55, 30720, price=590.0,
          core_name='Alder Lake-HX', socket='BGA1964', lanes=20, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i3 13th (Raptor Lake-U)
    S('intel', 16, 'Core i3 13th Generation', 12, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-U', socket='BGA1744',
        pcie='4.0', lanes=20, pcie_cfg='x4, x1', mem='DDR5-5200;DDR4-3200;LPDDR5-5200',
        ch=2, memmax=64, ecc=0, igpu='UHD Graphics', igpu_clk=300, igpu_boost=1250,
        igpu_cfg='64:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='OPI', multi=1,
        mem_bw=83.2), [
        C('Core i3-1315U', (2023, 1), 6, 8, 1200, 4500, 15, 10240, price=309.0),
        C('Core i3-1305U', (2023, 1), 5, 6, 1600, 4500, 15, 10240, price=309.0),
    ]),

    # ------------------------------------------------------------ Core i5 13th (Raptor Lake-U/P/H)
    S('intel', 17, 'Core i5 13th Generation', 13, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-U', socket='BGA1744',
        pcie='4.0', lanes=20, pcie_cfg='x4, x1', mem='DDR5-5200;DDR4-3200;LPDDR5-5200',
        ch=2, memmax=64, ecc=0, igpu='Iris Xe Graphics G7', igpu_clk=300, igpu_boost=1250,
        igpu_cfg='80:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='OPI', multi=1,
        mem_bw=83.2), [
        C('Core i5-1335U', (2023, 1), 10, 12, 1300, 4600, 15, 12288, price=340.0),
        C('Core i5-1340P', (2023, 1), 12, 16, 1900, 4600, 28, 12288, price=353.0,
          core_name='Raptor Lake-P', igpu_boost=1450),
        C('Core i5-13420H', (2023, 1), 8, 12, 2100, 4600, 45, 12288, price=342.0,
          core_name='Raptor Lake-H', lanes=28, pcie_cfg='x16, x4, x8', memmax=96),
        C('Core i5-13500H', (2023, 1), 12, 16, 2600, 4700, 45, 18432, price=342.0,
          core_name='Raptor Lake-H', lanes=28, pcie_cfg='x16, x4, x8', memmax=96),
    ]),

    # ------------------------------------------------------------ Core i7 13th (Raptor Lake-U/P/H)
    S('intel', 18, 'Core i7 13th Generation', 13, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-U', socket='BGA1744',
        pcie='4.0', lanes=20, pcie_cfg='x4, x1', mem='DDR5-5200;DDR4-3200;LPDDR5-5200',
        ch=2, memmax=64, ecc=0, igpu='Iris Xe Graphics G7', igpu_clk=300, igpu_boost=1300,
        igpu_cfg='96:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='OPI', multi=1,
        mem_bw=83.2), [
        C('Core i7-1355U', (2023, 1), 10, 12, 1700, 5000, 15, 12288, price=469.0),
        C('Core i7-1360P', (2023, 1), 12, 16, 2200, 5000, 28, 18432, price=480.0,
          core_name='Raptor Lake-P', igpu_boost=1500),
        C('Core i7-13620H', (2023, 1), 10, 16, 2400, 4900, 45, 24576, price=502.0,
          core_name='Raptor Lake-H', lanes=28, pcie_cfg='x16, x4, x8', memmax=96),
        C('Core i7-13700H', (2023, 1), 14, 20, 2400, 5000, 45, 24576, price=502.0,
          core_name='Raptor Lake-H', lanes=28, pcie_cfg='x16, x4, x8', memmax=96),
    ]),

    # ------------------------------------------------------------ Core i9 13th (Raptor Lake-H/HX)
    S('intel', 37, 'Core i9 13th Generation', 6, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-H', socket='BGA1744',
        pcie='5.0', lanes=28, pcie_cfg='x16, x4, x8', mem='DDR5-5200;DDR4-3200', ch=2,
        memmax=96, ecc=0, igpu='Iris Xe Graphics G7', igpu_clk=350, igpu_boost=1500,
        igpu_cfg='96:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=83.2), [
        C('Core i9-13900H', (2023, 1), 14, 20, 2600, 5400, 45, 24576, price=617.0),
        C('Core i9-13900HK', (2023, 1), 14, 20, 2600, 5400, 45, 24576, price=697.0, unlock=1),
        C('Core i9-13900HX', (2023, 1), 24, 32, 2200, 5400, 55, 36864, price=668.0,
          core_name='Raptor Lake-HX', socket='BGA1964', lanes=20, memmax=192, igpu_boost=1650),
        C('Core i9-13980HX', (2023, 1), 24, 32, 2200, 5600, 55, 36864, price=668.0,
          core_name='Raptor Lake-HX', socket='BGA1964', lanes=20, memmax=192, igpu_boost=1650),
    ]),

    # ------------------------------------------------------------ Core i5/i7/i9 14th (Raptor Lake-HX Refresh)
    S('intel', 17, 'Core i5 14th Generation', 14, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-HX Refresh', socket='BGA1964',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-5600;DDR4-3200', ch=2,
        memmax=192, ecc=0, igpu='UHD Graphics 770', igpu_clk=350, igpu_boost=1600,
        igpu_cfg='32:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=89.6), [
        C('Core i5-14500HX', (2024, 1), 14, 20, 2600, 4900, 55, 24576, price=337.0),
    ]),

    S('intel', 18, 'Core i7 14th Generation', 14, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-HX Refresh', socket='BGA1964',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-5600;DDR4-3200', ch=2,
        memmax=192, ecc=0, igpu='UHD Graphics 770', igpu_clk=350, igpu_boost=1600,
        igpu_cfg='32:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=89.6), [
        C('Core i7-14650HX', (2024, 1), 16, 24, 2200, 5200, 55, 30720, price=482.0),
        C('Core i7-14700HX', (2024, 1), 20, 28, 2100, 5500, 55, 33792, price=502.0),
    ]),

    S('intel', 37, 'Core i9 14th Generation', 7, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-HX Refresh', socket='BGA1964',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-5600;DDR4-3200', ch=2,
        memmax=192, ecc=0, igpu='UHD Graphics 770', igpu_clk=350, igpu_boost=1650,
        igpu_cfg='32:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=89.6), [
        C('Core i9-14900HX', (2024, 1), 24, 32, 2200, 5800, 55, 36864, price=668.0),
    ]),

    # ------------------------------------------------------------ Core Ultra Series 1 (Meteor Lake)
    S('intel', 38, 'Core Ultra 5 Series 1', 1, dict(
        fab=4, arch='Meteor Lake', core_name='Meteor Lake-H', socket='BGA2049',
        pcie='5.0', lanes=20, pcie_cfg='x8, x4, x1', mem='LPDDR5x-7467;DDR5-5600', ch=2,
        memmax=96, ecc=0, igpu='Arc Graphics', igpu_clk=600, igpu_boost=2200,
        igpu_cfg='7 Xe-Cores', isa=ISA_INTEL_ARL, feat=FEAT_HT, bus='OPI', multi=1,
        mem_bw=119.5), [
        C('Core Ultra 5 125H', (2023, 12), 14, 18, 1200, 4500, 28, 18432, price=375.0),
        C('Core Ultra 5 135H', (2023, 12), 14, 18, 1200, 4600, 28, 18432, price=375.0),
    ]),

    S('intel', 39, 'Core Ultra 7 Series 1', 1, dict(
        fab=4, arch='Meteor Lake', core_name='Meteor Lake-H', socket='BGA2049',
        pcie='5.0', lanes=20, pcie_cfg='x8, x4, x1', mem='LPDDR5x-7467;DDR5-5600', ch=2,
        memmax=96, ecc=0, igpu='Arc Graphics', igpu_clk=600, igpu_boost=2250,
        igpu_cfg='8 Xe-Cores', isa=ISA_INTEL_ARL, feat=FEAT_HT, bus='OPI', multi=1,
        mem_bw=119.5), [
        C('Core Ultra 7 155H', (2023, 12), 16, 22, 1400, 4800, 28, 24576, price=469.0),
        C('Core Ultra 7 165H', (2023, 12), 16, 22, 1400, 5000, 28, 24576, price=469.0),
    ]),

    S('intel', 40, 'Core Ultra 9 Series 1', 1, dict(
        fab=4, arch='Meteor Lake', core_name='Meteor Lake-H', socket='BGA2049',
        pcie='5.0', lanes=20, pcie_cfg='x8, x4, x1', mem='LPDDR5x-7467;DDR5-5600', ch=2,
        memmax=96, ecc=0, igpu='Arc Graphics', igpu_clk=600, igpu_boost=2350,
        igpu_cfg='8 Xe-Cores', isa=ISA_INTEL_ARL, feat=FEAT_HT, bus='OPI', multi=1,
        mem_bw=119.5), [
        C('Core Ultra 9 185H', (2023, 12), 16, 22, 1400, 5100, 45, 24576, price=640.0),
    ]),

    # ------------------------------------------------------------ Core Ultra Series 2 (Lunar Lake)
    S('intel', 38, 'Core Ultra 5 Series 2', 2, dict(
        fab=3, arch='Lunar Lake', core_name='Lunar Lake-MX', socket='BGA2833',
        pcie='5.0', lanes=12, pcie_cfg='x8, x4', mem='LPDDR5x-8533', ch=2, memmax=32,
        ecc=0, igpu='Arc Graphics 130V', igpu_clk=600, igpu_boost=1850, igpu_cfg='7 Xe2-Cores',
        isa=ISA_INTEL_ARL, feat=FEAT_PLAIN2, bus='OPI', multi=1, mem_bw=136.5), [
        C('Core Ultra 5 228V', (2024, 9), 8, 8, 2100, 4500, 17, 8192, price=475.0),
        C('Core Ultra 5 238V', (2024, 9), 8, 8, 2100, 4700, 17, 8192, price=475.0),
    ]),

    S('intel', 39, 'Core Ultra 7 Series 2', 2, dict(
        fab=3, arch='Lunar Lake', core_name='Lunar Lake-MX', socket='BGA2833',
        pcie='5.0', lanes=12, pcie_cfg='x8, x4', mem='LPDDR5x-8533', ch=2, memmax=32,
        ecc=0, igpu='Arc Graphics 140V', igpu_clk=600, igpu_boost=1950, igpu_cfg='8 Xe2-Cores',
        isa=ISA_INTEL_ARL, feat=FEAT_PLAIN2, bus='OPI', multi=1, mem_bw=136.5), [
        C('Core Ultra 7 258V', (2024, 9), 8, 8, 2200, 4800, 17, 12288, price=649.0),
        C('Core Ultra 7 268V', (2024, 9), 8, 8, 2200, 5000, 17, 12288, price=649.0),
    ]),

    S('intel', 40, 'Core Ultra 9 Series 2', 2, dict(
        fab=3, arch='Lunar Lake', core_name='Lunar Lake-MX', socket='BGA2833',
        pcie='5.0', lanes=12, pcie_cfg='x8, x4', mem='LPDDR5x-8533', ch=2, memmax=32,
        ecc=0, igpu='Arc Graphics 140V', igpu_clk=600, igpu_boost=2050, igpu_cfg='8 Xe2-Cores',
        isa=ISA_INTEL_ARL, feat=FEAT_PLAIN2, bus='OPI', multi=1, mem_bw=136.5), [
        C('Core Ultra 9 288V', (2024, 9), 8, 8, 3300, 5100, 30, 12288, price=899.0),
    ]),

    # ------------------------------------------------------------ Core Ultra Series 2 (Arrow Lake-H / HX)
    S('intel', 38, 'Core Ultra 5 Series 2H', 3, dict(
        fab=3, arch='Arrow Lake', core_name='Arrow Lake-H', socket='BGA2049',
        pcie='5.0', lanes=20, pcie_cfg='x8, x4, x1', mem='LPDDR5x-8400;DDR5-6400', ch=2,
        memmax=128, ecc=0, igpu='Arc Graphics', igpu_clk=600, igpu_boost=2100,
        igpu_cfg='7 Xe-Cores', isa=ISA_INTEL_ARL, feat=FEAT_PLAIN2, bus='OPI', multi=1,
        mem_bw=134.4), [
        C('Core Ultra 5 225H', (2025, 1), 14, 14, 2500, 4900, 28, 18432, price=375.0),
        C('Core Ultra 5 245H', (2025, 1), 14, 14, 2500, 5100, 28, 24576, price=375.0),
    ]),

    S('intel', 39, 'Core Ultra 7 Series 2H', 3, dict(
        fab=3, arch='Arrow Lake', core_name='Arrow Lake-H', socket='BGA2049',
        pcie='5.0', lanes=20, pcie_cfg='x8, x4, x1', mem='LPDDR5x-8400;DDR5-6400', ch=2,
        memmax=128, ecc=0, igpu='Arc Graphics', igpu_clk=600, igpu_boost=2200,
        igpu_cfg='8 Xe-Cores', isa=ISA_INTEL_ARL, feat=FEAT_PLAIN2, bus='OPI', multi=1,
        mem_bw=134.4), [
        C('Core Ultra 7 255H', (2025, 1), 16, 16, 2400, 5100, 28, 24576, price=469.0),
        C('Core Ultra 7 265H', (2025, 1), 16, 16, 2500, 5300, 28, 24576, price=469.0),
        C('Core Ultra 7 255HX', (2025, 1), 20, 20, 2300, 5200, 55, 30720, price=502.0,
          core_name='Arrow Lake-HX', socket='BGA2114', lanes=24, memmax=192),
    ]),

    S('intel', 40, 'Core Ultra 9 Series 2H', 3, dict(
        fab=3, arch='Arrow Lake', core_name='Arrow Lake-H', socket='BGA2049',
        pcie='5.0', lanes=20, pcie_cfg='x8, x4, x1', mem='LPDDR5x-8400;DDR5-6400', ch=2,
        memmax=128, ecc=0, igpu='Arc Graphics', igpu_clk=600, igpu_boost=2350,
        igpu_cfg='8 Xe-Cores', isa=ISA_INTEL_ARL, feat=FEAT_PLAIN2, bus='OPI', multi=1,
        mem_bw=134.4), [
        C('Core Ultra 9 285H', (2025, 1), 16, 16, 2900, 5400, 45, 24576, price=640.0),
        C('Core Ultra 9 275HX', (2025, 1), 24, 24, 2100, 5400, 55, 36864, price=668.0,
          core_name='Arrow Lake-HX', socket='BGA2114', lanes=24, memmax=192),
    ]),

    # ------------------------------------------------------------ Intel Processor N Series (Alder Lake-N / Twin Lake)
    S('intel', 41, 'Intel Processor N Series', 1, dict(
        fab=10, arch='Alder Lake', core_name='Alder Lake-N', socket='BGA1264',
        pcie='3.0', lanes=9, pcie_cfg='x2, x1', mem='DDR5-4800;DDR4-3200', ch=1,
        memmax=16, ecc=0, igpu='UHD Graphics', igpu_clk=300, igpu_boost=750,
        igpu_cfg='16:0:0', isa=ISA_INTEL_ADL, feat=FEAT_PLAIN2, bus='DMI 4.0', multi=1,
        mem_bw=38.4), [
        C('Processor N100', (2023, 1), 4, 4, 800, 3400, 6, 6144, price=55.0),
        C('Processor N200', (2023, 1), 4, 4, 1000, 3700, 6, 6144, price=193.0),
        C('Processor N150', (2024, 11), 4, 4, 800, 3600, 6, 6144, price=55.0),
        C('Processor N250', (2024, 11), 4, 4, 1000, 3800, 6, 6144, price=193.0),
    ]),

    # ------------------------------------------------------------ Pentium Silver / Celeron N (Jasper Lake)
    S('intel', 3, 'Pentium Silver', 21, dict(
        fab=10, arch='Jasper Lake', core_name='Jasper Lake', socket='BGA1338',
        pcie='3.0', lanes=8, pcie_cfg='x4, x1', mem='DDR4-2933;LPDDR4x-2933', ch=2,
        memmax=16, ecc=0, igpu='UHD Graphics 605', igpu_clk=400, igpu_boost=900,
        igpu_cfg='16:0:0', isa=ISA_INTEL_9, feat=FEAT_PLAIN2, bus='DMI 3.0', multi=1,
        mem_bw=46.9), [
        C('Pentium Silver N6005', (2021, 1), 4, 4, 2000, 3300, 10, 4096, price=161.0),
    ]),

    S('intel', 2, 'Celeron N Series', 7, dict(
        fab=10, arch='Jasper Lake', core_name='Jasper Lake', socket='BGA1338',
        pcie='3.0', lanes=8, pcie_cfg='x4, x1', mem='DDR4-2933;LPDDR4x-2933', ch=2,
        memmax=16, ecc=0, igpu='UHD Graphics 605', igpu_clk=400, igpu_boost=800,
        igpu_cfg='16:0:0', isa=ISA_INTEL_9, feat=FEAT_PLAIN2, bus='DMI 3.0', multi=1,
        mem_bw=46.9), [
        C('Celeron N5105', (2021, 1), 4, 4, 2000, 2900, 10, 4096, price=107.0),
        C('Celeron N4505', (2021, 1), 2, 2, 2000, 2900, 10, 4096, price=107.0),
    ]),
]
