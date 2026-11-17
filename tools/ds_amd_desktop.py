# -*- coding: utf-8 -*-
"""AMD desktop / HEDT CPUs released between 2018-11 and 2026-11."""

from ds_common import (C, S, ISA_AMD_ZEN, ISA_AMD_ZEN4, ISA_AMD_OLD,
                       FEAT_AMD_SMT, FEAT_AMD)

AM4 = dict(pcie='4.0', lanes=24, pcie_cfg='x16, x4, x4', mem='DDR4-3200', ch=2,
           memmax=128, ecc=0, socket='AM4', bus='Infinity Fabric', multi=1,
           mem_bw=51.2)
AM5 = dict(pcie='5.0', lanes=28, pcie_cfg='x16, x4, x4, x4', mem='DDR5-5200', ch=2,
           memmax=128, ecc=0, socket='AM5', bus='Infinity Fabric', multi=1,
           mem_bw=83.2)

AMD_DESKTOP = [

    # ------------------------------------------------------------ Ryzen 3 3000 (Matisse + Picasso)
    S('amd', 10, 'Ryzen 3 3000 Series', 9, dict(
        fab=7, arch='Zen 2', core_name='Matisse', pcie='4.0', lanes=24,
        pcie_cfg='x16, x4, x4', mem='DDR4-3200', ch=2, memmax=128, ecc=0,
        socket='AM4', igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=47.9), [
        C('Ryzen 3 3100', (2019, 7), 4, 8, 3600, 3900, 65, 16384, price=99.0),
        C('Ryzen 3 3300X', (2019, 7), 4, 8, 3800, 4300, 65, 16384, price=120.0, unlock=1),
        C('Ryzen 3 3200G', (2019, 9), 4, 4, 3600, 4000, 65, 4096, price=99.0,
          fab=12, arch='Zen+', core_name='Picasso', isa=ISA_AMD_OLD, feat=FEAT_AMD,
          igpu='Radeon Vega 8 Graphics', igpu_clk=1250, igpu_boost=None, igpu_cfg='8 CU',
          pcie='3.0', mem='DDR4-2933', mem_bw=43.7, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 5 3000
    S('amd', 10, 'Ryzen 5 3000 Series', 10, dict(
        fab=7, arch='Zen 2', core_name='Matisse', pcie='4.0', lanes=24,
        pcie_cfg='x16, x4, x4', mem='DDR4-3200', ch=2, memmax=128, ecc=0,
        socket='AM4', igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=47.9), [
        C('Ryzen 5 3500X', (2019, 9), 6, 6, 3600, 4100, 65, 32768, price=147.0,
          feat=FEAT_AMD, unlock=1),
        C('Ryzen 5 3600', (2019, 7), 6, 12, 3600, 4200, 65, 32768, price=199.0, unlock=1),
        C('Ryzen 5 3600X', (2019, 7), 6, 12, 3800, 4400, 95, 32768, price=249.0, unlock=1),
        C('Ryzen 5 3600XT', (2020, 7), 6, 12, 3800, 4500, 95, 32768, price=249.0, unlock=1),
        C('Ryzen 5 3400G', (2019, 9), 4, 8, 3700, 4200, 65, 4096, price=149.0,
          fab=12, arch='Zen+', core_name='Picasso', isa=ISA_AMD_OLD,
          igpu='Radeon Vega 11 Graphics', igpu_clk=1400, igpu_boost=None, igpu_cfg='11 CU',
          pcie='3.0', mem='DDR4-2933', mem_bw=43.7, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 7 3000
    S('amd', 10, 'Ryzen 7 3000 Series', 11, dict(
        fab=7, arch='Zen 2', core_name='Matisse', pcie='4.0', lanes=24,
        pcie_cfg='x16, x4, x4', mem='DDR4-3200', ch=2, memmax=128, ecc=0,
        socket='AM4', igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=47.9), [
        C('Ryzen 7 3700X', (2019, 7), 8, 16, 3600, 4400, 65, 32768, price=329.0, unlock=1),
        C('Ryzen 7 3800X', (2019, 7), 8, 16, 3900, 4500, 105, 32768, price=399.0, unlock=1),
        C('Ryzen 7 3800XT', (2020, 7), 8, 16, 3900, 4700, 105, 32768, price=399.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 9 3000 (new product family)
    S('amd', 39, 'Ryzen 9 3000 Series', 1, dict(
        fab=7, arch='Zen 2', core_name='Matisse', pcie='4.0', lanes=24,
        pcie_cfg='x16, x4, x4', mem='DDR4-3200', ch=2, memmax=128, ecc=0,
        socket='AM4', igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=47.9), [
        C('Ryzen 9 3900X', (2019, 7), 12, 24, 3800, 4600, 105, 65536, price=499.0, unlock=1),
        C('Ryzen 9 3900XT', (2020, 7), 12, 24, 3800, 4700, 105, 65536, price=499.0, unlock=1),
        C('Ryzen 9 3950X', (2019, 11), 16, 32, 3500, 4700, 105, 65536, price=749.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Threadripper 3000 (Castle Peak)
    S('amd', 10, 'Ryzen Threadripper 3000 Series', 12, dict(
        fab=7, arch='Zen 2', core_name='Castle Peak', socket='sTRX4', pcie='4.0',
        lanes=64, pcie_cfg='x16, x8, x4', mem='DDR4-3200', ch=4, memmax=256, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=102.4), [
        C('Ryzen Threadripper 3960X', (2019, 11), 24, 48, 3800, 4500, 280, 131072, price=1399.0,
          unlock=1),
        C('Ryzen Threadripper 3970X', (2019, 11), 32, 64, 3700, 4500, 280, 131072, price=1999.0,
          unlock=1),
        C('Ryzen Threadripper 3990X', (2020, 2), 64, 128, 2900, 4300, 280, 262144, price=3990.0,
          unlock=1),
    ]),

    # ------------------------------------------------------------ Threadripper PRO 3000
    S('amd', 10, 'Ryzen Threadripper PRO 3000 Series', 13, dict(
        fab=7, arch='Zen 2', core_name='Castle Peak', socket='sWRX8', pcie='4.0',
        lanes=128, pcie_cfg='x16, x8, x4', mem='DDR4-3200', ch=8, memmax=2048, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=2,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=204.8), [
        C('Ryzen Threadripper PRO 3945WX', (2020, 7), 12, 24, 4000, 4300, 280, 65536,
          price=2199.0, unlock=1),
        C('Ryzen Threadripper PRO 3975WX', (2020, 7), 32, 64, 3500, 4200, 280, 131072,
          price=3499.0, unlock=1),
        C('Ryzen Threadripper PRO 3995WX', (2020, 7), 64, 128, 2700, 4200, 280, 262144,
          price=5499.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 5 5000 (Vermeer + Cezanne)
    S('amd', 10, 'Ryzen 5 5000 Series', 14, dict(
        fab=7, arch='Zen 3', core_name='Vermeer', pcie='4.0', lanes=24,
        pcie_cfg='x16, x4, x4', mem='DDR4-3200', ch=2, memmax=128, ecc=0,
        socket='AM4', igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=51.2), [
        C('Ryzen 5 5600X', (2020, 11), 6, 12, 3700, 4600, 65, 32768, price=299.0, unlock=1),
        C('Ryzen 5 5600', (2022, 3), 6, 12, 3500, 4400, 65, 32768, price=199.0, unlock=1),
        C('Ryzen 5 5600X3D', (2023, 7), 6, 12, 3300, 4400, 105, 98304, price=229.0, unlock=1),
        C('Ryzen 5 5600G', (2021, 8), 6, 12, 3900, 4400, 65, 16384, price=259.0,
          core_name='Cezanne', igpu='Radeon Vega 7 Graphics', igpu_clk=1900,
          igpu_cfg='7 CU', unlock=1),
        C('Ryzen 5 5500', (2022, 4), 6, 12, 3600, 4200, 65, 16384, price=159.0,
          core_name='Cezanne', pcie='3.0', unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 7 5000
    S('amd', 10, 'Ryzen 7 5000 Series', 15, dict(
        fab=7, arch='Zen 3', core_name='Vermeer', pcie='4.0', lanes=24,
        pcie_cfg='x16, x4, x4', mem='DDR4-3200', ch=2, memmax=128, ecc=0,
        socket='AM4', igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=51.2), [
        C('Ryzen 7 5700X', (2022, 4), 8, 16, 3400, 4600, 65, 32768, price=299.0, unlock=1),
        C('Ryzen 7 5700X3D', (2024, 1), 8, 16, 3000, 4100, 105, 98304, price=249.0, unlock=1),
        C('Ryzen 7 5800X', (2020, 11), 8, 16, 3800, 4700, 105, 32768, price=449.0, unlock=1),
        C('Ryzen 7 5800X3D', (2022, 4), 8, 16, 3400, 4500, 105, 98304, price=449.0, unlock=1),
        C('Ryzen 7 5700G', (2021, 8), 8, 16, 3800, 4600, 65, 16384, price=359.0,
          core_name='Cezanne', igpu='Radeon Vega 8 Graphics', igpu_clk=2000,
          igpu_cfg='8 CU', unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 9 5000
    S('amd', 39, 'Ryzen 9 5000 Series', 2, dict(
        fab=7, arch='Zen 3', core_name='Vermeer', pcie='4.0', lanes=24,
        pcie_cfg='x16, x4, x4', mem='DDR4-3200', ch=2, memmax=128, ecc=0,
        socket='AM4', igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=51.2), [
        C('Ryzen 9 5900X', (2020, 11), 12, 24, 3700, 4800, 105, 65536, price=549.0, unlock=1),
        C('Ryzen 9 5950X', (2020, 11), 16, 32, 3400, 4900, 105, 65536, price=799.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Threadripper PRO 5000 (Chagall)
    S('amd', 10, 'Ryzen Threadripper PRO 5000 Series', 16, dict(
        fab=7, arch='Zen 3', core_name='Chagall', socket='sWRX8', pcie='4.0',
        lanes=128, pcie_cfg='x16, x8, x4', mem='DDR4-3200', ch=8, memmax=2048, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=2,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=204.8), [
        C('Ryzen Threadripper PRO 5965WX', (2022, 3), 24, 48, 3800, 4500, 280, 131072,
          price=2399.0, unlock=1),
        C('Ryzen Threadripper PRO 5975WX', (2022, 3), 32, 64, 3600, 4500, 280, 131072,
          price=3299.0, unlock=1),
        C('Ryzen Threadripper PRO 5995WX', (2022, 3), 64, 128, 2700, 4500, 280, 262144,
          price=6499.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 5 7000 (Raphael)
    S('amd', 10, 'Ryzen 5 7000 Series', 17, dict(
        fab=5, arch='Zen 4', core_name='Raphael', pcie='5.0', lanes=28,
        pcie_cfg='x16, x4, x4, x4', mem='DDR5-5200', ch=2, memmax=128, ecc=0,
        socket='AM5', igpu='Radeon Graphics', igpu_clk=400, igpu_boost=2200,
        igpu_cfg='2 CU', isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, mem_bw=83.2), [
        C('Ryzen 5 7600', (2023, 1), 6, 12, 3800, 5100, 65, 32768, price=229.0, unlock=1),
        C('Ryzen 5 7600X', (2022, 9), 6, 12, 4700, 5300, 105, 32768, price=299.0, unlock=1),
        C('Ryzen 5 7500F', (2023, 7), 6, 12, 3700, 5000, 65, 32768, price=179.0,
          igpu=None, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 7 7000
    S('amd', 10, 'Ryzen 7 7000 Series', 18, dict(
        fab=5, arch='Zen 4', core_name='Raphael', pcie='5.0', lanes=28,
        pcie_cfg='x16, x4, x4, x4', mem='DDR5-5200', ch=2, memmax=128, ecc=0,
        socket='AM5', igpu='Radeon Graphics', igpu_clk=400, igpu_boost=2200,
        igpu_cfg='2 CU', isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, mem_bw=83.2), [
        C('Ryzen 7 7700', (2023, 1), 8, 16, 3800, 5300, 65, 32768, price=329.0, unlock=1),
        C('Ryzen 7 7700X', (2022, 9), 8, 16, 4500, 5400, 105, 32768, price=399.0, unlock=1),
        C('Ryzen 7 7800X3D', (2023, 4), 8, 16, 4200, 5000, 120, 98304, price=449.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 9 7000
    S('amd', 39, 'Ryzen 9 7000 Series', 3, dict(
        fab=5, arch='Zen 4', core_name='Raphael', pcie='5.0', lanes=28,
        pcie_cfg='x16, x4, x4, x4', mem='DDR5-5200', ch=2, memmax=128, ecc=0,
        socket='AM5', igpu='Radeon Graphics', igpu_clk=400, igpu_boost=2200,
        igpu_cfg='2 CU', isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, mem_bw=83.2), [
        C('Ryzen 9 7900', (2023, 1), 12, 24, 3700, 5400, 65, 65536, price=429.0, unlock=1),
        C('Ryzen 9 7900X', (2022, 9), 12, 24, 4700, 5600, 170, 65536, price=549.0, unlock=1),
        C('Ryzen 9 7900X3D', (2023, 2), 12, 24, 4400, 5600, 120, 131072, price=599.0,
          unlock=1),
        C('Ryzen 9 7950X', (2022, 9), 16, 32, 4500, 5700, 170, 65536, price=699.0, unlock=1),
        C('Ryzen 9 7950X3D', (2023, 2), 16, 32, 4200, 5700, 120, 131072, price=699.0,
          unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 8000G (Phoenix, AM5)
    S('amd', 10, 'Ryzen 5 8000 Series', 19, dict(
        fab=4, arch='Zen 4', core_name='Phoenix', pcie='4.0', lanes=20,
        pcie_cfg='x16, x4', mem='DDR5-5200', ch=2, memmax=256, ecc=0, socket='AM5',
        igpu='Radeon 760M', igpu_clk=2800, igpu_boost=None, igpu_cfg='8 CU',
        isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=83.2), [
        C('Ryzen 5 8500G', (2024, 1), 6, 12, 3500, 5000, 65, 16384, price=179.0, unlock=1),
        C('Ryzen 5 8600G', (2024, 1), 6, 12, 4300, 5000, 65, 16384, price=229.0,
          igpu='Radeon 760M', unlock=1),
    ]),

    S('amd', 10, 'Ryzen 7 8000 Series', 20, dict(
        fab=4, arch='Zen 4', core_name='Phoenix', pcie='4.0', lanes=20,
        pcie_cfg='x16, x4', mem='DDR5-5200', ch=2, memmax=256, ecc=0, socket='AM5',
        igpu='Radeon 780M', igpu_clk=2900, igpu_boost=None, igpu_cfg='12 CU',
        isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=83.2), [
        C('Ryzen 7 8700F', (2024, 4), 8, 16, 4100, 5000, 65, 16384, igpu=None, unlock=1),
        C('Ryzen 7 8700G', (2024, 1), 8, 16, 4200, 5100, 65, 16384, price=329.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Ryzen 9000 (Granite Ridge)
    S('amd', 10, 'Ryzen 5 9000 Series', 21, dict(
        fab=4, arch='Zen 5', core_name='Granite Ridge', pcie='5.0', lanes=28,
        pcie_cfg='x16, x4, x4, x4', mem='DDR5-5600', ch=2, memmax=192, ecc=0,
        socket='AM5', igpu='Radeon Graphics', igpu_clk=400, igpu_boost=2200,
        igpu_cfg='2 CU', isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, mem_bw=89.6), [
        C('Ryzen 5 9600', (2025, 1), 6, 12, 3800, 5200, 65, 32768, price=189.0, unlock=1),
        C('Ryzen 5 9600X', (2024, 8), 6, 12, 3900, 5400, 65, 32768, price=279.0, unlock=1),
    ]),

    S('amd', 10, 'Ryzen 7 9000 Series', 22, dict(
        fab=4, arch='Zen 5', core_name='Granite Ridge', pcie='5.0', lanes=28,
        pcie_cfg='x16, x4, x4, x4', mem='DDR5-5600', ch=2, memmax=192, ecc=0,
        socket='AM5', igpu='Radeon Graphics', igpu_clk=400, igpu_boost=2200,
        igpu_cfg='2 CU', isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, mem_bw=89.6), [
        C('Ryzen 7 9700X', (2024, 8), 8, 16, 3800, 5500, 65, 32768, price=359.0, unlock=1),
        C('Ryzen 7 9800X3D', (2024, 11), 8, 16, 4700, 5200, 120, 98304, price=479.0, unlock=1),
    ]),

    S('amd', 39, 'Ryzen 9 9000 Series', 4, dict(
        fab=4, arch='Zen 5', core_name='Granite Ridge', pcie='5.0', lanes=28,
        pcie_cfg='x16, x4, x4, x4', mem='DDR5-5600', ch=2, memmax=192, ecc=0,
        socket='AM5', igpu='Radeon Graphics', igpu_clk=400, igpu_boost=2200,
        igpu_cfg='2 CU', isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric',
        multi=1, mem_bw=89.6), [
        C('Ryzen 9 9900X', (2024, 8), 12, 24, 4400, 5600, 120, 65536, price=499.0, unlock=1),
        C('Ryzen 9 9900X3D', (2025, 3), 12, 24, 4400, 5500, 120, 131072, price=599.0,
          unlock=1),
        C('Ryzen 9 9950X', (2024, 8), 16, 32, 4300, 5700, 170, 65536, price=649.0, unlock=1),
        C('Ryzen 9 9950X3D', (2025, 3), 16, 32, 4300, 5700, 170, 131072, price=699.0,
          unlock=1),
    ]),

    # ------------------------------------------------------------ Threadripper 7000 (Storm Peak)
    S('amd', 10, 'Ryzen Threadripper 7000 Series', 23, dict(
        fab=5, arch='Zen 4', core_name='Storm Peak', socket='sTR5', pcie='5.0',
        lanes=148, pcie_cfg='x16, x8, x4', mem='DDR5-5200', ch=4, memmax=1024, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=166.4), [
        C('Ryzen Threadripper 7960X', (2023, 11), 24, 48, 4200, 5300, 350, 131072,
          price=1499.0, unlock=1),
        C('Ryzen Threadripper 7970X', (2023, 11), 32, 64, 4000, 5300, 350, 131072,
          price=2499.0, unlock=1),
        C('Ryzen Threadripper 7980X', (2023, 11), 64, 128, 3200, 5100, 350, 262144,
          price=4999.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Threadripper PRO 7000
    S('amd', 10, 'Ryzen Threadripper PRO 7000 Series', 24, dict(
        fab=5, arch='Zen 4', core_name='Storm Peak', socket='sTR5', pcie='5.0',
        lanes=148, pcie_cfg='x16, x8, x4', mem='DDR5-5200', ch=8, memmax=2048, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=2,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=332.8), [
        C('Ryzen Threadripper PRO 7965WX', (2023, 11), 24, 48, 4200, 5300, 350, 131072,
          price=2649.0, unlock=1),
        C('Ryzen Threadripper PRO 7985WX', (2023, 11), 64, 128, 3200, 5100, 350, 262144,
          price=7349.0, unlock=1),
        C('Ryzen Threadripper PRO 7995WX', (2023, 11), 96, 192, 2500, 5100, 350, 393216,
          price=9999.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Threadripper 9000 (Shimada Peak)
    S('amd', 10, 'Ryzen Threadripper 9000 Series', 25, dict(
        fab=4, arch='Zen 5', core_name='Shimada Peak', socket='sTR5', pcie='5.0',
        lanes=148, pcie_cfg='x16, x8, x4', mem='DDR5-6400', ch=4, memmax=1024, ecc=1,
        igpu=None, isa=ISA_AMD_ZEN4, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1,
        igpu_clk=None, igpu_boost=None, igpu_cfg=None, mem_bw=204.8), [
        C('Ryzen Threadripper 9970X', (2025, 7), 32, 64, 4000, 5400, 350, 131072,
          price=2499.0, unlock=1),
        C('Ryzen Threadripper 9980X', (2025, 7), 64, 128, 3200, 5400, 350, 262144,
          price=4999.0, unlock=1),
        C('Ryzen Threadripper PRO 9995WX', (2025, 7), 96, 192, 2500, 5400, 350, 393216,
          price=11999.0, unlock=1),
    ]),

    # ------------------------------------------------------------ Athlon 3000G (Picasso)
    S('amd', 5, 'Athlon 3000 Series', 23, dict(
        fab=12, arch='Zen+', core_name='Picasso', socket='AM4', pcie='3.0', lanes=20,
        pcie_cfg='x16, x4', mem='DDR4-2933', ch=2, memmax=64, ecc=0,
        igpu='Radeon Vega 3 Graphics', igpu_clk=1100, igpu_boost=None, igpu_cfg='3 CU',
        isa=ISA_AMD_OLD, feat=FEAT_AMD_SMT, bus='Infinity Fabric', multi=1, mem_bw=43.7), [
        C('Athlon 3000G', (2019, 11), 2, 4, 3500, 3500, 35, 4096, price=49.0, unlock=1),
    ]),
]
