# -*- coding: utf-8 -*-
"""Intel desktop / HEDT CPUs released between 2018-11 and 2026-11."""

from ds_common import (C, S, ISA_INTEL_9, ISA_INTEL_512, ISA_INTEL_ADL, ISA_INTEL_ARL,
                       FEAT_HT, FEAT_PLAIN, FEAT_PLAIN2, PCIE_CFG16, PCIE_CFG20, PCIE_CFG24)

INTEL_DESKTOP = [

    # ------------------------------------------------------------ Core i3 10th (Comet Lake)
    S('intel', 5, 'Core i3 10th Generation', 10, dict(
        fab=14, arch='Comet Lake', core_name='Comet Lake-S', socket='LGA1200',
        pcie='3.0', lanes=16, pcie_cfg=PCIE_CFG16, mem='DDR4-2666', ch=2, memmax=128, ecc=0,
        igpu='UHD Graphics 630', igpu_clk=350, igpu_boost=1100, igpu_cfg='24:0:0',
        isa=ISA_INTEL_9, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=41.6), [
        C('Core i3-10100', (2020, 5), 4, 8, 3600, 4300, 65, 6144, price=122.0),
        C('Core i3-10100F', (2020, 10), 4, 8, 3600, 4300, 65, 6144, price=79.0, igpu=None),
        C('Core i3-10300', (2020, 5), 4, 8, 3700, 4400, 65, 8192, price=143.0),
        C('Core i3-10320', (2020, 5), 4, 8, 3800, 4600, 65, 8192, price=154.0),
        C('Core i3-10105', (2021, 3), 4, 8, 3700, 4400, 65, 6144, price=122.0),
        C('Core i3-10105F', (2021, 3), 4, 8, 3700, 4400, 65, 6144, price=97.0, igpu=None),
    ]),

    # ------------------------------------------------------------ Core i5 10th (Comet Lake)
    S('intel', 6, 'Core i5 10th Generation', 11, dict(
        fab=14, arch='Comet Lake', core_name='Comet Lake-S', socket='LGA1200',
        pcie='3.0', lanes=16, pcie_cfg=PCIE_CFG16, mem='DDR4-2666', ch=2, memmax=128, ecc=0,
        igpu='UHD Graphics 630', igpu_clk=350, igpu_boost=1200, igpu_cfg='24:0:0',
        isa=ISA_INTEL_9, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=41.6), [
        C('Core i5-10400', (2020, 5), 6, 12, 2900, 4300, 65, 12288, price=182.0),
        C('Core i5-10400F', (2020, 5), 6, 12, 2900, 4300, 65, 12288, price=157.0, igpu=None),
        C('Core i5-10500', (2020, 5), 6, 12, 3100, 4500, 65, 12288, price=192.0),
        C('Core i5-10600', (2020, 5), 6, 12, 3300, 4800, 65, 12288, price=213.0),
        C('Core i5-10600K', (2020, 5), 6, 12, 4100, 4800, 125, 12288, price=262.0, unlock=1),
        C('Core i5-10600KF', (2020, 5), 6, 12, 4100, 4800, 125, 12288, price=237.0,
          igpu=None, unlock=1),
        C('Core i5-10400T', (2020, 5), 6, 12, 2000, 3600, 35, 12288, igpu_boost=1050),
    ]),

    # ------------------------------------------------------------ Core i7 10th (Comet Lake)
    S('intel', 7, 'Core i7 10th Generation', 12, dict(
        fab=14, arch='Comet Lake', core_name='Comet Lake-S', socket='LGA1200',
        pcie='3.0', lanes=16, pcie_cfg=PCIE_CFG16, mem='DDR4-2933', ch=2, memmax=128, ecc=0,
        igpu='UHD Graphics 630', igpu_clk=350, igpu_boost=1200, igpu_cfg='24:0:0',
        isa=ISA_INTEL_9, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=45.8), [
        C('Core i7-10700', (2020, 5), 8, 16, 2900, 4800, 65, 16384, price=298.0),
        C('Core i7-10700F', (2020, 5), 8, 16, 2900, 4800, 65, 16384, price=298.0, igpu=None),
        C('Core i7-10700K', (2020, 5), 8, 16, 3800, 5100, 125, 16384, price=374.0, unlock=1),
        C('Core i7-10700KF', (2020, 5), 8, 16, 3800, 5100, 125, 16384, price=349.0,
          igpu=None, unlock=1),
        C('Core i7-10700T', (2020, 5), 8, 16, 2000, 4500, 35, 16384, igpu_boost=1050),
    ]),

    # ------------------------------------------------------------ Core i9 10th (Comet Lake + Cascade Lake-X)
    S('intel', 8, 'Core i9 10th Generation', 11, dict(
        fab=14, arch='Comet Lake', core_name='Comet Lake-S', socket='LGA1200',
        pcie='3.0', lanes=16, pcie_cfg=PCIE_CFG16, mem='DDR4-2933', ch=2, memmax=128, ecc=0,
        igpu='UHD Graphics 630', igpu_clk=350, igpu_boost=1200, igpu_cfg='24:0:0',
        isa=ISA_INTEL_9, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=45.8), [
        C('Core i9-10850K', (2020, 7), 10, 20, 3600, 5200, 125, 20480, price=453.0, unlock=1),
        C('Core i9-10900', (2020, 5), 10, 20, 2800, 5200, 65, 20480, price=439.0),
        C('Core i9-10900F', (2020, 5), 10, 20, 2800, 5200, 65, 20480, price=422.0, igpu=None),
        C('Core i9-10900K', (2020, 5), 10, 20, 3700, 5300, 125, 20480, price=488.0, unlock=1),
        C('Core i9-10900KF', (2020, 5), 10, 20, 3700, 5300, 125, 20480, price=464.0,
          igpu=None, unlock=1),
        C('Core i9-10900T', (2020, 5), 10, 20, 1900, 4600, 35, 20480, igpu_boost=1050),
        # Cascade Lake-X (LGA2066, no iGPU, quad channel)
        C('Core i9-10900X', (2019, 11), 10, 20, 3700, 4500, 165, 19712,
          socket='LGA2066', core_name='Cascade Lake-X', mem='DDR4-2933', ch=4, memmax=256,
          lanes=48, pcie_cfg='x48, x32, x16, x8, x4', igpu=None, unlock=1, ecc=0,
          price=590.0, mem_bw=93.8, bus='DMI 3.0', multi=1),
        C('Core i9-10920X', (2019, 11), 12, 24, 3500, 4800, 165, 19712,
          socket='LGA2066', core_name='Cascade Lake-X', mem='DDR4-2933', ch=4, memmax=256,
          lanes=48, pcie_cfg='x48, x32, x16, x8, x4', igpu=None, unlock=1, ecc=0,
          price=713.0, mem_bw=93.8, bus='DMI 3.0', multi=1),
        C('Core i9-10940X', (2019, 11), 14, 28, 3300, 4800, 165, 19712,
          socket='LGA2066', core_name='Cascade Lake-X', mem='DDR4-2933', ch=4, memmax=256,
          lanes=48, pcie_cfg='x48, x32, x16, x8, x4', igpu=None, unlock=1, ecc=0,
          price=784.0, mem_bw=93.8, bus='DMI 3.0', multi=1),
        C('Core i9-10980XE', (2019, 11), 18, 36, 3000, 4800, 165, 25344,
          socket='LGA2066', core_name='Cascade Lake-X', mem='DDR4-2933', ch=4, memmax=256,
          lanes=48, pcie_cfg='x48, x32, x16, x8, x4', igpu=None, unlock=1, ecc=0,
          price=979.0, mem_bw=93.8, bus='DMI 3.0', multi=1),
    ]),

    # ------------------------------------------------------------ Core i5 11th (Rocket Lake)
    S('intel', 6, 'Core i5 11th Generation', 13, dict(
        fab=14, arch='Rocket Lake', core_name='Rocket Lake-S', socket='LGA1200',
        pcie='4.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR4-3200', ch=2, memmax=128, ecc=0,
        igpu='UHD Graphics 750', igpu_clk=350, igpu_boost=1300, igpu_cfg='32:0:0',
        isa=ISA_INTEL_512, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=50.0), [
        C('Core i5-11400', (2021, 3), 6, 12, 2600, 4400, 65, 12288, price=182.0),
        C('Core i5-11400F', (2021, 3), 6, 12, 2600, 4400, 65, 12288, price=157.0, igpu=None),
        C('Core i5-11500', (2021, 3), 6, 12, 2700, 4600, 65, 12288, price=192.0),
        C('Core i5-11600', (2021, 3), 6, 12, 2800, 4800, 65, 12288, price=213.0),
        C('Core i5-11600K', (2021, 3), 6, 12, 3900, 4900, 125, 12288, price=262.0, unlock=1),
        C('Core i5-11600KF', (2021, 3), 6, 12, 3900, 4900, 125, 12288, price=237.0,
          igpu=None, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i7 11th (Rocket Lake)
    S('intel', 7, 'Core i7 11th Generation', 14, dict(
        fab=14, arch='Rocket Lake', core_name='Rocket Lake-S', socket='LGA1200',
        pcie='4.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR4-3200', ch=2, memmax=128, ecc=0,
        igpu='UHD Graphics 750', igpu_clk=350, igpu_boost=1300, igpu_cfg='32:0:0',
        isa=ISA_INTEL_512, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=50.0), [
        C('Core i7-11700', (2021, 3), 8, 16, 2500, 4900, 65, 16384, price=323.0),
        C('Core i7-11700F', (2021, 3), 8, 16, 2500, 4900, 65, 16384, price=298.0, igpu=None),
        C('Core i7-11700K', (2021, 3), 8, 16, 3600, 5000, 125, 16384, price=399.0, unlock=1),
        C('Core i7-11700KF', (2021, 3), 8, 16, 3600, 5000, 125, 16384, price=374.0,
          igpu=None, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i9 11th (Rocket Lake)
    S('intel', 8, 'Core i9 11th Generation', 12, dict(
        fab=14, arch='Rocket Lake', core_name='Rocket Lake-S', socket='LGA1200',
        pcie='4.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR4-3200', ch=2, memmax=128, ecc=0,
        igpu='UHD Graphics 750', igpu_clk=350, igpu_boost=1300, igpu_cfg='32:0:0',
        isa=ISA_INTEL_512, feat=FEAT_HT, bus='DMI 3.0', multi=1, mem_bw=50.0), [
        C('Core i9-11900', (2021, 3), 8, 16, 2500, 5200, 65, 16384, price=439.0),
        C('Core i9-11900F', (2021, 3), 8, 16, 2500, 5200, 65, 16384, price=422.0, igpu=None),
        C('Core i9-11900K', (2021, 3), 8, 16, 3500, 5300, 125, 16384, price=539.0, unlock=1),
        C('Core i9-11900KF', (2021, 3), 8, 16, 3500, 5300, 125, 16384, price=513.0,
          igpu=None, unlock=1),
        C('Core i9-11900T', (2021, 3), 8, 16, 1500, 4900, 35, 16384, igpu_boost=1300),
    ]),

    # ------------------------------------------------------------ Core i3 12th (Alder Lake)
    S('intel', 5, 'Core i3 12th Generation', 15, dict(
        fab=10, arch='Alder Lake', core_name='Alder Lake-S', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-4800;DDR4-3200', ch=2,
        memmax=128, ecc=0, igpu='UHD Graphics 730', igpu_clk=300, igpu_boost=1400,
        igpu_cfg='24:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=76.8), [
        C('Core i3-12100', (2022, 1), 4, 8, 3300, 4300, 60, 12288, price=122.0),
        C('Core i3-12100F', (2022, 1), 4, 8, 3300, 4300, 58, 12288, price=97.0, igpu=None),
        C('Core i3-12300', (2022, 1), 4, 8, 3500, 4400, 60, 12288, price=143.0),
    ]),

    # ------------------------------------------------------------ Core i5 12th (Alder Lake)
    S('intel', 6, 'Core i5 12th Generation', 16, dict(
        fab=10, arch='Alder Lake', core_name='Alder Lake-S', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-4800;DDR4-3200', ch=2,
        memmax=128, ecc=0, igpu='UHD Graphics 730', igpu_clk=300, igpu_boost=1450,
        igpu_cfg='24:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=76.8), [
        C('Core i5-12400', (2022, 1), 6, 12, 2500, 4400, 65, 18432, price=192.0),
        C('Core i5-12400F', (2022, 1), 6, 12, 2500, 4400, 65, 18432, price=167.0, igpu=None),
        C('Core i5-12490F', (2022, 1), 6, 12, 3000, 4600, 65, 20480, igpu=None),
        C('Core i5-12500', (2022, 1), 6, 12, 3000, 4600, 65, 18432, price=202.0,
          igpu='UHD Graphics 770', igpu_boost=1450, igpu_cfg='32:0:0'),
        C('Core i5-12600', (2022, 1), 6, 12, 3300, 4800, 65, 18432, price=223.0,
          igpu='UHD Graphics 770', igpu_boost=1450, igpu_cfg='32:0:0'),
        C('Core i5-12600K', (2021, 11), 10, 16, 3700, 4900, 125, 20480, price=289.0,
          igpu='UHD Graphics 770', igpu_boost=1450, igpu_cfg='32:0:0', unlock=1),
        C('Core i5-12600KF', (2021, 11), 10, 16, 3700, 4900, 125, 20480, price=264.0,
          igpu=None, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i7 12th (Alder Lake)
    S('intel', 7, 'Core i7 12th Generation', 17, dict(
        fab=10, arch='Alder Lake', core_name='Alder Lake-S', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-4800;DDR4-3200', ch=2,
        memmax=128, ecc=0, igpu='UHD Graphics 770', igpu_clk=300, igpu_boost=1500,
        igpu_cfg='32:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=76.8), [
        C('Core i7-12700', (2022, 1), 12, 20, 2100, 4900, 65, 25600, price=339.0),
        C('Core i7-12700F', (2022, 1), 12, 20, 2100, 4900, 65, 25600, price=314.0, igpu=None),
        C('Core i7-12700K', (2021, 11), 12, 20, 3600, 5000, 125, 25600, price=409.0, unlock=1),
        C('Core i7-12700KF', (2021, 11), 12, 20, 3600, 5000, 125, 25600, price=384.0,
          igpu=None, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i9 12th (Alder Lake)
    S('intel', 8, 'Core i9 12th Generation', 13, dict(
        fab=10, arch='Alder Lake', core_name='Alder Lake-S', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-4800;DDR4-3200', ch=2,
        memmax=128, ecc=0, igpu='UHD Graphics 770', igpu_clk=300, igpu_boost=1550,
        igpu_cfg='32:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=76.8), [
        C('Core i9-12900', (2022, 1), 16, 24, 2400, 5100, 65, 30720, price=489.0),
        C('Core i9-12900F', (2022, 1), 16, 24, 2400, 5100, 65, 30720, price=464.0, igpu=None),
        C('Core i9-12900K', (2021, 11), 16, 24, 3200, 5200, 125, 30720, price=589.0, unlock=1),
        C('Core i9-12900KF', (2021, 11), 16, 24, 3200, 5200, 125, 30720, price=564.0,
          igpu=None, unlock=1),
        C('Core i9-12900KS', (2022, 4), 16, 24, 3400, 5500, 150, 30720, price=739.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i3 13th (Raptor Lake)
    S('intel', 5, 'Core i3 13th Generation', 18, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-S', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-4800;DDR4-3200', ch=2,
        memmax=128, ecc=0, igpu='UHD Graphics 730', igpu_clk=300, igpu_boost=1500,
        igpu_cfg='24:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=76.8), [
        C('Core i3-13100', (2023, 1), 4, 8, 3400, 4500, 60, 12288, price=134.0),
        C('Core i3-13100F', (2023, 1), 4, 8, 3400, 4500, 58, 12288, price=109.0, igpu=None),
    ]),

    # ------------------------------------------------------------ Core i5 13th (Raptor Lake)
    S('intel', 6, 'Core i5 13th Generation', 19, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-S', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-4800;DDR4-3200', ch=2,
        memmax=128, ecc=0, igpu='UHD Graphics 730', igpu_clk=300, igpu_boost=1550,
        igpu_cfg='24:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=76.8), [
        C('Core i5-13400', (2023, 1), 10, 16, 2500, 4600, 65, 20480, price=221.0),
        C('Core i5-13400F', (2023, 1), 10, 16, 2500, 4600, 65, 20480, price=196.0, igpu=None),
        C('Core i5-13500', (2023, 1), 14, 20, 2500, 4800, 65, 24576, price=232.0,
          igpu='UHD Graphics 770', igpu_boost=1550, igpu_cfg='32:0:0'),
        C('Core i5-13600', (2023, 1), 14, 20, 2700, 5000, 65, 24576, price=255.0,
          igpu='UHD Graphics 770', igpu_boost=1550, igpu_cfg='32:0:0'),
        C('Core i5-13600K', (2022, 10), 14, 20, 3500, 5100, 125, 24576, price=319.0,
          igpu='UHD Graphics 770', igpu_boost=1500, igpu_cfg='32:0:0', unlock=1),
        C('Core i5-13600KF', (2022, 10), 14, 20, 3500, 5100, 125, 24576, price=294.0,
          igpu=None, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i7 13th (Raptor Lake)
    S('intel', 7, 'Core i7 13th Generation', 20, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-S', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-5600;DDR4-3200', ch=2,
        memmax=192, ecc=0, igpu='UHD Graphics 770', igpu_clk=300, igpu_boost=1600,
        igpu_cfg='32:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=89.6), [
        C('Core i7-13700', (2023, 1), 16, 24, 2100, 5200, 65, 30720, price=384.0),
        C('Core i7-13700F', (2023, 1), 16, 24, 2100, 5200, 65, 30720, price=359.0, igpu=None),
        C('Core i7-13700K', (2022, 10), 16, 24, 3400, 5400, 125, 30720, price=409.0, unlock=1),
        C('Core i7-13700KF', (2022, 10), 16, 24, 3400, 5400, 125, 30720, price=384.0,
          igpu=None, unlock=1),
        C('Core i7-13790F', (2023, 2), 16, 24, 2100, 5200, 65, 33792, igpu=None),
    ]),

    # ------------------------------------------------------------ Core i9 13th (Raptor Lake)
    S('intel', 8, 'Core i9 13th Generation', 14, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-S', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-5600;DDR4-3200', ch=2,
        memmax=192, ecc=0, igpu='UHD Graphics 770', igpu_clk=300, igpu_boost=1650,
        igpu_cfg='32:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=89.6), [
        C('Core i9-13900', (2023, 1), 24, 32, 2000, 5600, 65, 36864, price=549.0),
        C('Core i9-13900F', (2023, 1), 24, 32, 2000, 5600, 65, 36864, price=524.0, igpu=None),
        C('Core i9-13900K', (2022, 10), 24, 32, 3000, 5800, 125, 36864, price=589.0, unlock=1),
        C('Core i9-13900KF', (2022, 10), 24, 32, 3000, 5800, 125, 36864, price=564.0,
          igpu=None, unlock=1),
        C('Core i9-13900KS', (2023, 1), 24, 32, 3200, 6000, 150, 36864, price=699.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i3 14th (Raptor Lake Refresh)
    S('intel', 5, 'Core i3 14th Generation', 21, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-S Refresh', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-4800;DDR4-3200', ch=2,
        memmax=128, ecc=0, igpu='UHD Graphics 730', igpu_clk=300, igpu_boost=1500,
        igpu_cfg='24:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=76.8), [
        C('Core i3-14100', (2024, 1), 4, 8, 3500, 4700, 60, 12288, price=134.0),
        C('Core i3-14100F', (2024, 1), 4, 8, 3500, 4700, 58, 12288, price=109.0, igpu=None),
    ]),

    # ------------------------------------------------------------ Core i5 14th (Raptor Lake Refresh)
    S('intel', 6, 'Core i5 14th Generation', 22, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-S Refresh', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-5600;DDR4-3200', ch=2,
        memmax=192, ecc=0, igpu='UHD Graphics 730', igpu_clk=300, igpu_boost=1550,
        igpu_cfg='24:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=89.6), [
        C('Core i5-14400', (2024, 1), 10, 16, 2500, 4700, 65, 20480, price=221.0),
        C('Core i5-14400F', (2024, 1), 10, 16, 2500, 4700, 65, 20480, price=196.0, igpu=None),
        C('Core i5-14500', (2024, 1), 14, 20, 2600, 5000, 65, 24576, price=232.0,
          igpu='UHD Graphics 770', igpu_cfg='32:0:0'),
        C('Core i5-14600', (2024, 1), 14, 20, 2700, 5200, 65, 24576, price=255.0,
          igpu='UHD Graphics 770', igpu_cfg='32:0:0'),
        C('Core i5-14600K', (2023, 10), 14, 20, 3500, 5300, 125, 24576, price=319.0,
          igpu='UHD Graphics 770', igpu_cfg='32:0:0', unlock=1),
        C('Core i5-14600KF', (2023, 10), 14, 20, 3500, 5300, 125, 24576, price=294.0,
          igpu=None, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i7 14th (Raptor Lake Refresh)
    S('intel', 7, 'Core i7 14th Generation', 23, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-S Refresh', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-5600;DDR4-3200', ch=2,
        memmax=192, ecc=0, igpu='UHD Graphics 770', igpu_clk=300, igpu_boost=1600,
        igpu_cfg='32:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=89.6), [
        C('Core i7-14700', (2024, 1), 20, 28, 2100, 5400, 65, 33792, price=384.0),
        C('Core i7-14700F', (2024, 1), 20, 28, 2100, 5400, 65, 33792, price=359.0, igpu=None),
        C('Core i7-14700K', (2023, 10), 20, 28, 3400, 5600, 125, 33792, price=409.0, unlock=1),
        C('Core i7-14700KF', (2023, 10), 20, 28, 3400, 5600, 125, 33792, price=384.0,
          igpu=None, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i9 14th (Raptor Lake Refresh)
    S('intel', 8, 'Core i9 14th Generation', 15, dict(
        fab=10, arch='Raptor Lake', core_name='Raptor Lake-S Refresh', socket='LGA1700',
        pcie='5.0', lanes=20, pcie_cfg=PCIE_CFG20, mem='DDR5-5600;DDR4-3200', ch=2,
        memmax=192, ecc=0, igpu='UHD Graphics 770', igpu_clk=300, igpu_boost=1650,
        igpu_cfg='32:0:0', isa=ISA_INTEL_ADL, feat=FEAT_HT, bus='DMI 4.0', multi=1,
        mem_bw=89.6), [
        C('Core i9-14900', (2024, 1), 24, 32, 2000, 5800, 65, 36864, price=549.0),
        C('Core i9-14900F', (2024, 1), 24, 32, 2000, 5800, 65, 36864, price=524.0, igpu=None),
        C('Core i9-14900K', (2023, 10), 24, 32, 3200, 6000, 125, 36864, price=589.0, unlock=1),
        C('Core i9-14900KF', (2023, 10), 24, 32, 3200, 6000, 125, 36864, price=564.0,
          igpu=None, unlock=1),
        C('Core i9-14900KS', (2024, 3), 24, 32, 3200, 6200, 150, 36864, price=689.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Core i3 N Series (Alder Lake-N)
    S('intel', 5, 'Core i3 N Series', 24, dict(
        fab=10, arch='Alder Lake', core_name='Alder Lake-N', socket='BGA1264',
        pcie='3.0', lanes=9, pcie_cfg='x2, x1', mem='DDR5-4800;DDR4-3200', ch=1,
        memmax=16, ecc=0, igpu='UHD Graphics', igpu_clk=300, igpu_boost=1250,
        igpu_cfg='32:0:0', isa=ISA_INTEL_ADL, feat=FEAT_PLAIN2, bus='DMI 4.0', multi=1,
        mem_bw=38.4), [
        C('Core i3-N300', (2023, 1), 8, 8, 1800, 3800, 7, 6144, price=309.0),
        C('Core i3-N305', (2023, 1), 8, 8, 1800, 3800, 15, 6144, price=309.0, igpu_boost=1250),
    ]),

    # ------------------------------------------------------------ Core Ultra 5 Series 2 (Arrow Lake-S)
    S('intel', 42, 'Core Ultra 5 Series 2', 1, dict(
        fab=3, arch='Arrow Lake', core_name='Arrow Lake-S', socket='LGA1851',
        pcie='5.0', lanes=24, pcie_cfg=PCIE_CFG24, mem='DDR5-6400', ch=2, memmax=192,
        ecc=0, igpu='Arc Graphics', igpu_clk=300, igpu_boost=1800, igpu_cfg='4 Xe-Cores',
        isa=ISA_INTEL_ARL, feat=FEAT_PLAIN2, bus='DMI 4.0', multi=1, mem_bw=102.4), [
        C('Core Ultra 5 225', (2025, 1), 10, 10, 3300, 4900, 65, 20480, price=246.0),
        C('Core Ultra 5 235', (2025, 1), 14, 14, 3400, 5000, 65, 24576, price=257.0),
        C('Core Ultra 5 245K', (2024, 10), 14, 14, 4200, 5200, 125, 24576, price=309.0,
          unlock=1),
        C('Core Ultra 5 245KF', (2024, 10), 14, 14, 4200, 5200, 125, 24576, price=294.0,
          igpu=None, unlock=1),
    ]),

    # ------------------------------------------------------------ Core Ultra 7 Series 2 (Arrow Lake-S)
    S('intel', 43, 'Core Ultra 7 Series 2', 1, dict(
        fab=3, arch='Arrow Lake', core_name='Arrow Lake-S', socket='LGA1851',
        pcie='5.0', lanes=24, pcie_cfg=PCIE_CFG24, mem='DDR5-6400', ch=2, memmax=192,
        ecc=0, igpu='Arc Graphics', igpu_clk=300, igpu_boost=1900, igpu_cfg='4 Xe-Cores',
        isa=ISA_INTEL_ARL, feat=FEAT_PLAIN2, bus='DMI 4.0', multi=1, mem_bw=102.4), [
        C('Core Ultra 7 265K', (2024, 10), 20, 20, 3900, 5500, 125, 30720, price=394.0,
          unlock=1),
        C('Core Ultra 7 265KF', (2024, 10), 20, 20, 3900, 5500, 125, 30720, price=379.0,
          igpu=None, unlock=1),
    ]),

    # ------------------------------------------------------------ Core Ultra 9 Series 2 (Arrow Lake-S)
    S('intel', 44, 'Core Ultra 9 Series 2', 1, dict(
        fab=3, arch='Arrow Lake', core_name='Arrow Lake-S', socket='LGA1851',
        pcie='5.0', lanes=24, pcie_cfg=PCIE_CFG24, mem='DDR5-6400', ch=2, memmax=192,
        ecc=0, igpu='Arc Graphics', igpu_clk=300, igpu_boost=2000, igpu_cfg='4 Xe-Cores',
        isa=ISA_INTEL_ARL, feat=FEAT_PLAIN2, bus='DMI 4.0', multi=1, mem_bw=102.4), [
        C('Core Ultra 9 285K', (2024, 10), 24, 24, 3700, 5700, 125, 36864, price=589.0,
          unlock=1),
    ]),
]
