# -*- coding: utf-8 -*-
"""Build the updated `cpus_db` JSON (structure identical to the 2018 original)."""

import json
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parent
sys.path.insert(0, str(WORK))

from ds_intel_desktop import INTEL_DESKTOP
from ds_intel_mobile import INTEL_MOBILE
from ds_intel_server import INTEL_SERVER
from ds_amd_desktop import AMD_DESKTOP
from ds_amd_mobile import AMD_MOBILE
from ds_amd_server import AMD_SERVER

SRC = WORK / 'payload' / 'cpus_db'
DST = WORK / 'payload' / 'cpus_db.new'

QUARTER = {1: 'Q1', 2: 'Q1', 3: 'Q1', 4: 'Q2', 5: 'Q2', 6: 'Q2',
           7: 'Q3', 8: 'Q3', 9: 'Q3', 10: 'Q4', 11: 'Q4', 12: 'Q4'}

# ---------------------------------------------------------------- new product families
NEW_PRODUCTS = [
    # vendor, id, product_name, family, type, order_product
    ('intel', 38, 'Core Ultra 5', 'coreultra5', 'mb', 12),
    ('intel', 39, 'Core Ultra 7', 'coreultra7', 'mb', 13),
    ('intel', 40, 'Core Ultra 9', 'coreultra9', 'mb', 14),
    ('intel', 41, 'Intel Processor', 'processor', 'dk', 11),
    ('intel', 42, 'Core Ultra 5', 'coreultra5', 'dk', 13),
    ('intel', 43, 'Core Ultra 7', 'coreultra7', 'dk', 14),
    ('intel', 44, 'Core Ultra 9', 'coreultra9', 'dk', 15),
    ('amd', 39, 'Ryzen 9', 'ryzen9', 'dk', 11),
    ('amd', 40, 'Ryzen 9', 'ryzen9', 'mb', 13),
    ('amd', 41, 'Ryzen AI', 'ryzenai', 'mb', 14),
]

# ---------------------------------------------------------------- L2 overrides (KB)
L2_MAP = {
    # Alder Lake-S
    'Core i3-12100': 5120, 'Core i3-12100F': 5120, 'Core i3-12300': 5120,
    'Core i5-12400': 7680, 'Core i5-12400F': 7680, 'Core i5-12490F': 7680,
    'Core i5-12500': 7680, 'Core i5-12600': 7680,
    'Core i5-12600K': 9728, 'Core i5-12600KF': 9728,
    'Core i7-12700': 12288, 'Core i7-12700F': 12288,
    'Core i7-12700K': 12288, 'Core i7-12700KF': 12288,
    'Core i9-12900': 14336, 'Core i9-12900F': 14336, 'Core i9-12900K': 14336,
    'Core i9-12900KF': 14336, 'Core i9-12900KS': 14336,
    # Raptor Lake-S
    'Core i3-13100': 5120, 'Core i3-13100F': 5120,
    'Core i5-13400': 9728, 'Core i5-13400F': 9728,
    'Core i5-13500': 20480, 'Core i5-13600': 20480,
    'Core i5-13600K': 20480, 'Core i5-13600KF': 20480,
    'Core i7-13700': 24576, 'Core i7-13700F': 24576, 'Core i7-13700K': 24576,
    'Core i7-13700KF': 24576, 'Core i7-13790F': 24576,
    'Core i9-13900': 32768, 'Core i9-13900F': 32768, 'Core i9-13900K': 32768,
    'Core i9-13900KF': 32768, 'Core i9-13900KS': 32768,
    # Raptor Lake-S Refresh
    'Core i3-14100': 5120, 'Core i3-14100F': 5120,
    'Core i5-14400': 9728, 'Core i5-14400F': 9728,
    'Core i5-14500': 20480, 'Core i5-14600': 20480,
    'Core i5-14600K': 20480, 'Core i5-14600KF': 20480,
    'Core i7-14700': 28672, 'Core i7-14700F': 28672,
    'Core i7-14700K': 28672, 'Core i7-14700KF': 28672,
    'Core i9-14900': 32768, 'Core i9-14900F': 32768, 'Core i9-14900K': 32768,
    'Core i9-14900KF': 32768, 'Core i9-14900KS': 32768,
    # Arrow Lake-S
    'Core Ultra 5 225': 22528, 'Core Ultra 5 235': 26624,
    'Core Ultra 5 245K': 26624, 'Core Ultra 5 245KF': 26624,
    'Core Ultra 7 265K': 36864, 'Core Ultra 7 265KF': 36864,
    'Core Ultra 9 285K': 40960,
    # Alder Lake mobile
    'Core i3-1215U': 4608, 'Core i3-1220P': 6656,
    'Core i5-1235U': 6656, 'Core i5-1240P': 9216,
    'Core i5-12450H': 7168, 'Core i5-12500H': 9216,
    'Core i7-1255U': 6656, 'Core i7-1260P': 9216, 'Core i7-1280P': 11776,
    'Core i7-12650H': 9728, 'Core i7-12700H': 11776,
    'Core i9-12900H': 11776, 'Core i9-12900HK': 11776, 'Core i9-12950HX': 14336,
    # Raptor Lake mobile
    'Core i3-1315U': 8192, 'Core i3-1305U': 8192,
    'Core i5-1335U': 12288, 'Core i5-1340P': 16384,
    'Core i5-13420H': 12288, 'Core i5-13500H': 16384,
    'Core i7-1355U': 12288, 'Core i7-1360P': 16384,
    'Core i7-13620H': 16384, 'Core i7-13700H': 20480,
    'Core i9-13900H': 20480, 'Core i9-13900HK': 20480,
    'Core i9-13900HX': 32768, 'Core i9-13980HX': 32768,
    'Core i5-14500HX': 20480, 'Core i7-14650HX': 24576,
    'Core i7-14700HX': 28672, 'Core i9-14900HX': 32768,
    # Meteor Lake
    'Core Ultra 5 125H': 14336, 'Core Ultra 5 135H': 14336,
    'Core Ultra 7 155H': 18432, 'Core Ultra 7 165H': 18432,
    'Core Ultra 9 185H': 18432,
    # Lunar Lake
    'Core Ultra 5 228V': 12288, 'Core Ultra 5 238V': 12288,
    'Core Ultra 7 258V': 12288, 'Core Ultra 7 268V': 12288,
    'Core Ultra 9 288V': 12288,
    # Arrow Lake-H / HX
    'Core Ultra 5 225H': 20480, 'Core Ultra 5 245H': 26624,
    'Core Ultra 7 255H': 26624, 'Core Ultra 7 265H': 26624,
    'Core Ultra 7 255HX': 36864,
    'Core Ultra 9 285H': 26624, 'Core Ultra 9 275HX': 40960,
}


def build():
    data = json.loads(SRC.read_text(encoding='utf-8'))
    order = {t: list(data[t][0].keys()) for t in data}
    next_id = {t: max(int(r['id']) for r in data[t]) + 1 for t in data}
    # cpu_data ids run in a separate sequence from cpu ids
    next_id['intel_cpu_data'] = max(int(r['id']) for r in data['intel_cpu_data']) + 1
    next_id['amd_cpu_data'] = max(int(r['id']) for r in data['amd_cpu_data']) + 1

    def row(table, values):
        return {k: values.get(k) for k in order[table]}

    # --- new products -------------------------------------------------------
    for vendor, pid, pname, family, ptype, porder in NEW_PRODUCTS:
        existing = {p['id'] for p in data[f'{vendor}_products']}
        if str(pid) in existing:
            raise SystemExit(f'product id {pid} already used for {vendor}')
        data[f'{vendor}_products'].append(row(f'{vendor}_products', {
            'id': str(pid), 'product_name': pname, 'family': family,
            'order_product': str(porder), 'type': ptype,
        }))

    series_defs = INTEL_DESKTOP + INTEL_MOBILE + INTEL_SERVER + \
        AMD_DESKTOP + AMD_MOBILE + AMD_SERVER

    added = {'series': 0, 'cpu': 0, 'data': 0}
    per_vendor = {'intel': 0, 'amd': 0}

    for sd in series_defs:
        vendor = sd['vendor']
        pid = sd['product']
        products = {p['id']: p for p in data[f'{vendor}_products']}
        if str(pid) not in products:
            raise SystemExit(f'missing product {vendor}/{pid} for series {sd["name"]}')

        sid = str(next_id[f'{vendor}_series'])
        next_id[f'{vendor}_series'] += 1
        data[f'{vendor}_series'].append(row(f'{vendor}_series', {
            'id': sid, 'id_product_family': str(pid),
            'serie_name': sd['name'], 'order_family': str(sd['order']),
        }))
        added['series'] += 1

        d = sd['defaults']
        for i, cpu in enumerate(sd['cpus'], start=1):
            model = cpu['model']
            full = model if model.startswith(('Intel ', 'AMD ')) else None
            if full is None:
                full = ('Intel ' + model) if vendor == 'intel' else ('AMD ' + model)

            cores = cpu['cores']
            threads = cpu['threads']
            base = cpu['base']
            boost = cpu['boost']
            year, month = cpu['ym']
            launch_str = f'{QUARTER[month]} {year}'
            launch_int = year * 100 + month

            cid = str(next_id[f'{vendor}_cpu'])
            next_id[f'{vendor}_cpu'] += 1

            data[f'{vendor}_cpu'].append(row(f'{vendor}_cpu', {
                'id': cid, 'id_serie': sid, 'order_number': str(i),
                'name': full, 'launch': str(launch_int), 'cores': str(cores),
                'core_clk': str(base), 'core_clk_max': str(boost),
            }))
            added['cpu'] += 1

            did = str(next_id[f'{vendor}_cpu_data'])
            next_id[f'{vendor}_cpu_data'] += 1

            isa = cpu.get('isa', d['isa'])

            l3 = cpu['l3']
            if model in L2_MAP:
                l2 = L2_MAP[model]
            elif cpu.get('arch', d['arch']) in ('Zen 4', 'Zen 5', 'Zen 4c', 'Zen 5c'):
                l2 = cores * 1024
            elif vendor == 'amd':
                l2 = cores * 512
            else:
                l2 = cores * 256

            arch = cpu.get('arch', d['arch'])
            if vendor == 'amd' and arch.startswith('Zen') and arch not in ('Zen+', 'Zen 2', 'Zen 3'):
                l1i, l1d = 32 * cores, 32 * cores
            elif vendor == 'amd':
                l1i, l1d = 64 * cores, 32 * cores
            else:
                l1i, l1d = 32 * cores, 32 * cores

            unlock = cpu.get('unlock', d.get('mult_unlock', 0))
            igpu = cpu.get('igpu', d.get('igpu'))
            price = cpu.get('price')

            data[f'{vendor}_cpu_data'].append(row(f'{vendor}_cpu_data', {
                'id': did, 'id_cpu': cid, 'name': full, 'variant': None,
                'launch': launch_str,
                'lauch_price': None if price is None else f'{price:.1f}',
                'part_number': None,
                'core_arch': arch,
                'core_name': cpu.get('core_name', d.get('core_name')),
                'core_stepping': None, 'sspec': None,
                'fab': str(cpu.get('fab', d.get('fab'))),
                'transistor_count': None, 'die_size': None, 'pkg_size': None,
                'tdp': f"{cpu['tdp']:.1f}",
                'socket': cpu.get('socket', d.get('socket')),
                'core_clk': f'{base:.1f}', 'core_clk_boost': f'{boost:.1f}',
                'core_clk_boost_detail': None,
                'cores': str(cores), 'threads': str(threads),
                'multiplier': f'{base / 100:.1f}', 'multiplier_max': f'{boost / 100:.1f}',
                'multiplier_unlock': str(1 if unlock else 0),
                'cache_l1_inst': str(l1i), 'cache_l1_data': str(l1d),
                'cache_l2': str(l2), 'cache_l3': str(l3),
                'cache_l4': None,
                'bus': d.get('bus'), 'bus_clk': None, 'bus_speed': None,
                'data_width': '64',
                'instruction_set': isa,
                'features': cpu.get('feat', d.get('feat')),
                'pcie_revision': cpu.get('pcie', d.get('pcie')),
                'pcie_lanes': str(cpu.get('lanes', d.get('lanes'))),
                'pcie_config': cpu.get('pcie_cfg', d.get('pcie_cfg')),
                'mem_type': cpu.get('mem', d.get('mem')),
                'mem_ecc': str(cpu.get('ecc', d.get('ecc', 0))),
                'mem_bandwidth': None if cpu.get('mem_bw', d.get('mem_bw')) is None
                else f"{cpu.get('mem_bw', d.get('mem_bw')):.1f}",
                'mem_max': str(cpu.get('memmax', d.get('memmax'))),
                'mem_channels': str(cpu.get('ch', d.get('ch'))),
                'max_temp': None, 'vcore': None,
                'graphics_name': igpu,
                'graphics_clk': None if igpu is None else
                str(cpu.get('igpu_clk', d.get('igpu_clk')) or 0),
                'graphics_clk_boost': None if igpu is None else
                (str(cpu.get('igpu_boost')) if cpu.get('igpu_boost') else None),
                'graphics_core_config': None if igpu is None else
                cpu.get('igpu_cfg', d.get('igpu_cfg')),
                'multi_cpus': str(cpu.get('multi', d.get('multi', 1))),
                'notes': cpu.get('notes'),
                'bm_cinebenchr15_single': None, 'bm_cinebenchr15_multi': None,
                'bm_geekbench4_single': None, 'bm_geekbench4_multi': None,
                'bm_passmark': None,
                'released': '1', 'image_cpu': '0', 'image_author': None,
            }))
            added['data'] += 1
            per_vendor[vendor] += 1

    DST.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')),
                   encoding='utf-8')

    print(f'new series     : {added["series"]}')
    print(f'new cpu rows   : {added["cpu"]}  (intel {per_vendor["intel"]}, '
          f'amd {per_vendor["amd"]})')
    print(f'new data rows  : {added["data"]}')
    print()
    for t in ('intel_products', 'intel_series', 'intel_cpu', 'intel_cpu_data',
              'amd_products', 'amd_series', 'amd_cpu', 'amd_cpu_data'):
        print(f'{t:18} {len(data[t]):5} rows')
    print()
    print(f'written: {DST}  ({DST.stat().st_size / 1048576:.2f} MB)')


ISA_ZEN4_SHORT = None  # placeholder, replaced below

if __name__ == '__main__':
    from ds_common import ISA_AMD_ZEN4
    ISA_ZEN4_SHORT = ISA_AMD_ZEN4
    build()
