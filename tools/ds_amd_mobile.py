# -*- coding: utf-8 -*-
"""AMD mobile CPUs released between 2018-11 and 2026-11."""

from ds_common import C, S, ISA_AMD_ZEN, ISA_AMD_ZEN4, ISA_AMD_OLD, FEAT_AMD_SMT, FEAT_AMD

FP5 = dict(socket='FP7', pcie='5.0', lanes=16, pcie_cfg='x8, x4', mem='DDR5-5600;LPDDR5x-7500',
           ch=2, memmax=256, ecc=0, bus='Infinity Fabric', multi=1, mem_bw=89.6)

AMD_MOBILE = [

    # ------------------------------------------------------------ Ryzen 3 3000 (Picasso)
    S('amd', 35, 'Ryzen 3 3000 Series', 4, dict(
        fab=12, arch='Zen+', core_name='Picasso', socket='FP5', pcie='3.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR4-2400', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 3 Graphics', igpu_clk=1200, igpu_boost=None, igpu_cfg='3 CU',
        isa=ISA_AMD_OLD, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=38.4), [
        C('Ryzen 3 3200U', (2019, 1), 2, 4, 2600, 3500, 15, 4096, price=149.0),
        C('Ryzen 3 3250U', (2020, 1), 2, 4, 2600, 3500, 15, 4096, price=149.0),
        C('Ryzen 3 3300U', (2019, 1), 4, 4, 2100, 3500, 15, 4096, price=179.0,
          feat=FEAT_AMD),
    ]),

    # ------------------------------------------------------------ Ryzen 5 3000 (mobile)
    S('amd', 35, 'Ryzen 5 3000 Series', 5, dict(
        fab=12, arch='Zen+', core_name='Picasso', socket='FP5', pcie='3.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR4-2400', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 8 Graphics', igpu_clk=1200, igpu_boost=None, igpu_cfg='8 CU',
        isa=ISA_AMD_OLD, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=38.4), [
        C('Ryzen 5 3500U', (2019, 1), 4, 8, 2100, 3700, 15, 4096, price=209.0),
        C('Ryzen 5 3550H', (2019, 1), 4, 8, 2100, 3700, 35, 4096, price=209.0),
        C('Ryzen 5 3580U', (2019, 10), 4, 8, 2100, 3700, 15, 4096, price=229.0),
    ]),

    # ------------------------------------------------------------ Ryzen 7 3000 (mobile)
    S('amd', 35, 'Ryzen 7 3000 Series', 6, dict(
        fab=12, arch='Zen+', core_name='Picasso', socket='FP5', pcie='3.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR4-2400', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 10 Graphics', igpu_clk=1400, igpu_boost=None, igpu_cfg='10 CU',
        isa=ISA_AMD_OLD, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=38.4), [
        C('Ryzen 7 3700U', (2019, 1), 4, 8, 2300, 4000, 15, 4096, price=279.0),
        C('Ryzen 7 3750H', (2019, 1), 4, 8, 2300, 4000, 35, 4096, price=279.0),
        C('Ryzen 7 3780U', (2019, 10), 4, 8, 2300, 4000, 15, 4096, price=299.0),
    ]),

    # ------------------------------------------------------------ Ryzen 3 4000 (Renoir)
    S('amd', 35, 'Ryzen 3 4000 Series', 7, dict(
        fab=7, arch='Zen 2', core_name='Renoir', socket='FP6', pcie='3.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR4-3200;LPDDR4x-4266', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 5 Graphics', igpu_clk=1500, igpu_boost=None, igpu_cfg='5 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD, bus='Infinity Fabric', multi=1, mem_bw=51.2), [
        C('Ryzen 3 4300U', (2020, 1), 4, 4, 2700, 3700, 15, 4096, price=169.0),
    ]),

    # ------------------------------------------------------------ Ryzen 5 4000 (Renoir)
    S('amd', 35, 'Ryzen 5 4000 Series', 8, dict(
        fab=7, arch='Zen 2', core_name='Renoir', socket='FP6', pcie='3.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR4-3200;LPDDR4x-4266', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 6 Graphics', igpu_clk=1500, igpu_boost=None, igpu_cfg='6 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=51.2), [
        C('Ryzen 5 4500U', (2020, 1), 6, 6, 2300, 4000, 15, 8192, price=229.0,
          igpu='Radeon Vega 6 Graphics', feat=FEAT_AMD),
        C('Ryzen 5 4600U', (2020, 1), 6, 12, 2100, 4000, 15, 8192, price=249.0),
        C('Ryzen 5 4600H', (2020, 1), 6, 12, 3000, 4000, 45, 8192, price=249.0,
          igpu='Radeon Vega 6 Graphics'),
    ]),

    # ------------------------------------------------------------ Ryzen 7 4000 (Renoir)
    S('amd', 35, 'Ryzen 7 4000 Series', 9, dict(
        fab=7, arch='Zen 2', core_name='Renoir', socket='FP6', pcie='3.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR4-3200;LPDDR4x-4266', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 7 Graphics', igpu_clk=1600, igpu_boost=None, igpu_cfg='7 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=51.2), [
        C('Ryzen 7 4700U', (2020, 1), 8, 8, 2000, 4100, 15, 8192, price=329.0,
          igpu='Radeon Vega 7 Graphics', feat=FEAT_AMD),
        C('Ryzen 7 4800U', (2020, 1), 8, 16, 1800, 4200, 15, 8192, price=379.0,
          igpu='Radeon Vega 8 Graphics'),
        C('Ryzen 7 4800H', (2020, 1), 8, 16, 2900, 4200, 45, 8192, price=379.0,
          igpu='Radeon Vega 7 Graphics'),
        C('Ryzen 7 4800HS', (2020, 1), 8, 16, 2900, 4200, 35, 8192, price=379.0,
          igpu='Radeon Vega 7 Graphics'),
    ]),

    # ------------------------------------------------------------ Ryzen 9 4000 (Renoir)
    S('amd', 40, 'Ryzen 9 4000 Series', 1, dict(
        fab=7, arch='Zen 2', core_name='Renoir', socket='FP6', pcie='3.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR4-3200;LPDDR4x-4266', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 8 Graphics', igpu_clk=1750, igpu_boost=None, igpu_cfg='8 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=51.2), [
        C('Ryzen 9 4900HS', (2020, 3), 8, 16, 3000, 4300, 35, 8192, price=499.0),
        C('Ryzen 9 4900H', (2020, 3), 8, 16, 3300, 4400, 45, 8192, price=499.0),
    ]),

    # ------------------------------------------------------------ Ryzen 3 5000 (mobile)
    S('amd', 35, 'Ryzen 3 5000 Series', 10, dict(
        fab=7, arch='Zen 2', core_name='Lucienne', socket='FP6', pcie='3.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR4-3200;LPDDR4x-4266', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 6 Graphics', igpu_clk=1500, igpu_boost=None, igpu_cfg='6 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=51.2), [
        C('Ryzen 3 5300U', (2021, 1), 4, 8, 2600, 3800, 15, 4096, price=179.0),
        C('Ryzen 3 5425U', (2022, 1), 4, 8, 2700, 4100, 15, 8192, price=179.0,
          arch='Zen 3', core_name='Barcelo-R', isa=ISA_AMD_ZEN),
    ]),

    # ------------------------------------------------------------ Ryzen 5 5000 (mobile)
    S('amd', 35, 'Ryzen 5 5000 Series', 11, dict(
        fab=7, arch='Zen 2', core_name='Lucienne', socket='FP6', pcie='3.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR4-3200;LPDDR4x-4266', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 7 Graphics', igpu_clk=1800, igpu_boost=None, igpu_cfg='7 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=51.2), [
        C('Ryzen 5 5500U', (2021, 1), 6, 12, 2100, 4000, 15, 8192, price=249.0),
        C('Ryzen 5 5600U', (2021, 1), 6, 12, 2300, 4200, 15, 16384, price=269.0,
          arch='Zen 3', core_name='Cezanne', igpu_clk=1800),
        C('Ryzen 5 5600H', (2021, 1), 6, 12, 3300, 4200, 45, 16384, price=269.0,
          arch='Zen 3', core_name='Cezanne', igpu_clk=1800),
        C('Ryzen 5 5600HS', (2021, 1), 6, 12, 3000, 4200, 35, 16384, price=269.0,
          arch='Zen 3', core_name='Cezanne', igpu_clk=1800),
    ]),

    # ------------------------------------------------------------ Ryzen 7 5000 (mobile)
    S('amd', 35, 'Ryzen 7 5000 Series', 12, dict(
        fab=7, arch='Zen 2', core_name='Lucienne', socket='FP6', pcie='3.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR4-3200;LPDDR4x-4266', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 8 Graphics', igpu_clk=1800, igpu_boost=None, igpu_cfg='8 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=51.2), [
        C('Ryzen 7 5700U', (2021, 1), 8, 16, 1800, 4300, 15, 8192, price=379.0),
        C('Ryzen 7 5800U', (2021, 1), 8, 16, 1900, 4400, 15, 16384, price=449.0,
          arch='Zen 3', core_name='Cezanne', igpu_clk=2000),
        C('Ryzen 7 5800H', (2021, 1), 8, 16, 3200, 4400, 45, 16384, price=449.0,
          arch='Zen 3', core_name='Cezanne', igpu_clk=2000),
        C('Ryzen 7 5800HS', (2021, 1), 8, 16, 2800, 4400, 35, 16384, price=449.0,
          arch='Zen 3', core_name='Cezanne', igpu_clk=2000),
        C('Ryzen 7 5825U', (2022, 1), 8, 16, 2000, 4500, 15, 16384, price=449.0,
          arch='Zen 3', core_name='Barcelo-R', igpu_clk=2000),
    ]),

    # ------------------------------------------------------------ Ryzen 9 5000 (mobile)
    S('amd', 40, 'Ryzen 9 5000 Series', 2, dict(
        fab=7, arch='Zen 3', core_name='Cezanne', socket='FP6', pcie='3.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR4-3200;LPDDR4x-4266', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 8 Graphics', igpu_clk=2100, igpu_boost=None, igpu_cfg='8 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=51.2), [
        C('Ryzen 9 5900HS', (2021, 1), 8, 16, 3000, 4600, 35, 16384, price=599.0),
        C('Ryzen 9 5900HX', (2021, 1), 8, 16, 3300, 4600, 45, 16384, price=599.0, unlock=1),
        C('Ryzen 9 5980HX', (2021, 1), 8, 16, 3300, 4800, 45, 16384, price=649.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 5 6000 (Rembrandt)
    S('amd', 35, 'Ryzen 5 6000 Series', 13, dict(
        fab=6, arch='Zen 3+', core_name='Rembrandt', socket='FP7', pcie='4.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR5-4800;LPDDR5-6400', ch=2, memmax=64, ecc=0,
        igpu='Radeon 660M', igpu_clk=1900, igpu_boost=None, igpu_cfg='6 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=76.8), [
        C('Ryzen 5 6600U', (2022, 1), 6, 12, 2900, 4500, 15, 16384, price=279.0),
        C('Ryzen 5 6600H', (2022, 1), 6, 12, 3300, 4500, 45, 16384, price=279.0),
    ]),

    # ------------------------------------------------------------ Ryzen 7 6000 (Rembrandt)
    S('amd', 35, 'Ryzen 7 6000 Series', 14, dict(
        fab=6, arch='Zen 3+', core_name='Rembrandt', socket='FP7', pcie='4.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR5-4800;LPDDR5-6400', ch=2, memmax=64, ecc=0,
        igpu='Radeon 680M', igpu_clk=2200, igpu_boost=None, igpu_cfg='12 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=76.8), [
        C('Ryzen 7 6800U', (2022, 1), 8, 16, 2700, 4700, 15, 16384, price=449.0),
        C('Ryzen 7 6800H', (2022, 1), 8, 16, 3200, 4700, 45, 16384, price=449.0),
        C('Ryzen 7 6800HS', (2022, 1), 8, 16, 3200, 4700, 35, 16384, price=449.0),
    ]),

    # ------------------------------------------------------------ Ryzen 9 6000 (Rembrandt)
    S('amd', 40, 'Ryzen 9 6000 Series', 3, dict(
        fab=6, arch='Zen 3+', core_name='Rembrandt', socket='FP7', pcie='4.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR5-4800;LPDDR5-6400', ch=2, memmax=64, ecc=0,
        igpu='Radeon 680M', igpu_clk=2400, igpu_boost=None, igpu_cfg='12 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=76.8), [
        C('Ryzen 9 6900HX', (2022, 1), 8, 16, 3300, 4900, 45, 16384, price=699.0, unlock=1),
        C('Ryzen 9 6980HX', (2022, 1), 8, 16, 3300, 5000, 45, 16384, price=749.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 3 7000 (Mendocino)
    S('amd', 35, 'Ryzen 3 7000 Series', 15, dict(
        fab=6, arch='Zen 2', core_name='Mendocino', socket='FT6', pcie='3.0', lanes=10,
        pcie_cfg='x4, x2, x1', mem='LPDDR5-5500', ch=2, memmax=16, ecc=0,
        igpu='Radeon 610M', igpu_clk=1900, igpu_boost=None, igpu_cfg='2 CU',
        isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=88.0), [
        C('Ryzen 3 7320U', (2023, 1), 4, 8, 2400, 4100, 15, 4096, price=199.0),
    ]),

    # ------------------------------------------------------------ Ryzen 5 7000 (Mendocino / Phoenix / Dragon Range)
    S('amd', 35, 'Ryzen 5 7000 Series', 16, dict(
        fab=4, arch='Zen 4', core_name='Phoenix', socket='FP7', pcie='4.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR5-5600;LPDDR5x-7500', ch=2, memmax=256, ecc=0,
        igpu='Radeon 660M', igpu_clk=1900, igpu_boost=None, igpu_cfg='6 CU',
        isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=89.6), [
        C('Ryzen 5 7520U', (2023, 1), 4, 8, 2800, 4300, 15, 4096, price=229.0,
          fab=6, core_name='Mendocino', socket='FT6', pcie='3.0', lanes=10,
          mem='LPDDR5-5500', memmax=16, igpu='Radeon 610M', isa=ISA_AMD_ZEN),
        C('Ryzen 5 7530U', (2023, 1), 6, 12, 2000, 4500, 15, 16384, price=229.0,
          fab=7, arch='Zen 3', core_name='Barcelo-R', socket='FP6', pcie='3.0',
          mem='DDR4-3200;LPDDR4x-4266', memmax=64, igpu='Radeon Vega 7 Graphics',
          igpu_clk=2000, isa=ISA_AMD_ZEN),
        C('Ryzen 5 7640U', (2023, 5), 6, 12, 3500, 4900, 15, 16384, price=249.0),
        C('Ryzen 5 7640HS', (2023, 5), 6, 12, 4300, 5000, 35, 16384, price=249.0),
        C('Ryzen 5 7645HX', (2023, 1), 6, 12, 4000, 5000, 55, 32768, price=249.0,
          core_name='Dragon Range', socket='FL1', pcie='5.0', lanes=28,
          pcie_cfg='x16, x4, x4, x4', mem='DDR5-5200', memmax=64, igpu='Radeon 610M'),
    ]),

    # ------------------------------------------------------------ Ryzen 7 7000 (Phoenix / Rembrandt-R / Dragon Range)
    S('amd', 35, 'Ryzen 7 7000 Series', 17, dict(
        fab=4, arch='Zen 4', core_name='Phoenix', socket='FP7', pcie='4.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR5-5600;LPDDR5x-7500', ch=2, memmax=256, ecc=0,
        igpu='Radeon 780M', igpu_clk=2700, igpu_boost=None, igpu_cfg='12 CU',
        isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=89.6), [
        C('Ryzen 7 7730U', (2023, 1), 8, 16, 2000, 4500, 15, 16384, price=349.0,
          fab=7, arch='Zen 3', core_name='Barcelo-R', socket='FP6', pcie='3.0',
          mem='DDR4-3200;LPDDR4x-4266', memmax=64, igpu='Radeon Vega 8 Graphics',
          igpu_clk=2000, isa=ISA_AMD_ZEN),
        C('Ryzen 7 7735U', (2023, 1), 8, 16, 2700, 4750, 28, 16384, price=349.0,
          fab=6, arch='Zen 3+', core_name='Rembrandt-R', igpu='Radeon 680M',
          igpu_clk=2200, isa=ISA_AMD_ZEN),
        C('Ryzen 7 7735HS', (2023, 1), 8, 16, 3200, 4750, 35, 16384, price=349.0,
          fab=6, arch='Zen 3+', core_name='Rembrandt-R', igpu='Radeon 680M',
          igpu_clk=2200, isa=ISA_AMD_ZEN),
        C('Ryzen 7 7840U', (2023, 5), 8, 16, 3300, 5100, 28, 16384, price=399.0),
        C('Ryzen 7 7840HS', (2023, 5), 8, 16, 3800, 5100, 35, 16384, price=399.0),
        C('Ryzen 7 7745HX', (2023, 1), 8, 16, 3600, 5100, 55, 32768, price=399.0,
          core_name='Dragon Range', socket='FL1', pcie='5.0', lanes=28,
          pcie_cfg='x16, x4, x4, x4', mem='DDR5-5200', memmax=64, igpu='Radeon 610M',
          igpu_clk=2200),
    ]),

    # ------------------------------------------------------------ Ryzen 9 7000 (Phoenix / Dragon Range)
    S('amd', 40, 'Ryzen 9 7000 Series', 4, dict(
        fab=4, arch='Zen 4', core_name='Phoenix', socket='FP7', pcie='4.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR5-5600;LPDDR5x-7500', ch=2, memmax=256, ecc=0,
        igpu='Radeon 780M', igpu_clk=2800, igpu_boost=None, igpu_cfg='12 CU',
        isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=89.6), [
        C('Ryzen 9 7940HS', (2023, 5), 8, 16, 4000, 5200, 35, 16384, price=599.0, unlock=1),
        C('Ryzen 9 7945HX', (2023, 1), 16, 32, 2500, 5400, 55, 65536, price=699.0,
          core_name='Dragon Range', socket='FL1', pcie='5.0', lanes=28,
          pcie_cfg='x16, x4, x4, x4', mem='DDR5-5200', memmax=64, igpu='Radeon 610M',
          igpu_clk=2200, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 5 8000 (Hawk Point)
    S('amd', 35, 'Ryzen 5 8000 Series', 18, dict(
        fab=4, arch='Zen 4', core_name='Hawk Point', socket='FP7', pcie='4.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR5-5600;LPDDR5x-7500', ch=2, memmax=256, ecc=0,
        igpu='Radeon 760M', igpu_clk=2600, igpu_boost=None, igpu_cfg='8 CU',
        isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=89.6), [
        C('Ryzen 5 8540U', (2024, 1), 6, 12, 3200, 4900, 15, 16384, price=269.0),
        C('Ryzen 5 8640U', (2024, 1), 6, 12, 3500, 4900, 15, 16384, price=269.0),
        C('Ryzen 5 8645HS', (2024, 1), 6, 12, 4300, 5000, 45, 16384, price=269.0),
    ]),

    # ------------------------------------------------------------ Ryzen 7 8000 (Hawk Point)
    S('amd', 35, 'Ryzen 7 8000 Series', 19, dict(
        fab=4, arch='Zen 4', core_name='Hawk Point', socket='FP7', pcie='4.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR5-5600;LPDDR5x-7500', ch=2, memmax=256, ecc=0,
        igpu='Radeon 780M', igpu_clk=2700, igpu_boost=None, igpu_cfg='12 CU',
        isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=89.6), [
        C('Ryzen 7 8840U', (2024, 1), 8, 16, 3300, 5100, 28, 16384, price=399.0),
        C('Ryzen 7 8845HS', (2024, 1), 8, 16, 3800, 5100, 45, 16384, price=399.0),
    ]),

    # ------------------------------------------------------------ Ryzen 9 8000 (Hawk Point)
    S('amd', 40, 'Ryzen 9 8000 Series', 5, dict(
        fab=4, arch='Zen 4', core_name='Hawk Point', socket='FP7', pcie='4.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR5-5600;LPDDR5x-7500', ch=2, memmax=256, ecc=0,
        igpu='Radeon 780M', igpu_clk=2800, igpu_boost=None, igpu_cfg='12 CU',
        isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=89.6), [
        C('Ryzen 9 8945HS', (2024, 1), 8, 16, 4000, 5200, 45, 16384, price=599.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen AI 300 (Strix Point)
    S('amd', 41, 'Ryzen AI 300 Series', 1, dict(
        fab=4, arch='Zen 5', core_name='Strix Point', socket='FP8', pcie='5.0', lanes=16,
        pcie_cfg='x8, x4', mem='DDR5-5600;LPDDR5x-7500', ch=2, memmax=256, ecc=0,
        igpu='Radeon 890M', igpu_clk=2900, igpu_boost=None, igpu_cfg='16 CU',
        isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=120.0), [
        C('Ryzen AI 9 365', (2024, 7), 10, 20, 2000, 5000, 28, 24576, price=499.0),
        C('Ryzen AI 9 HX 370', (2024, 7), 12, 24, 2000, 5100, 28, 24576, price=599.0,
          igpu='Radeon 890M'),
        C('Ryzen AI 7 PRO 360', (2024, 10), 8, 16, 2000, 5000, 28, 16384, price=419.0,
          igpu='Radeon 880M', igpu_cfg='12 CU'),
    ]),

    # ------------------------------------------------------------ Ryzen AI Max 300 (Strix Halo)
    S('amd', 41, 'Ryzen AI Max 300 Series', 2, dict(
        fab=4, arch='Zen 5', core_name='Strix Halo', socket='FP11', pcie='5.0', lanes=16,
        pcie_cfg='x16, x8, x4', mem='LPDDR5x-8000', ch=4, memmax=128, ecc=0,
        igpu='Radeon 8060S', igpu_clk=2900, igpu_boost=None, igpu_cfg='40 CU',
        isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=256.0), [
        C('Ryzen AI Max+ 395', (2025, 2), 16, 32, 3000, 5100, 55, 65536, price=1299.0),
        C('Ryzen AI Max 390', (2025, 2), 12, 24, 3000, 5100, 55, 65536, price=999.0,
          igpu='Radeon 8050S'),
    ]),
]
