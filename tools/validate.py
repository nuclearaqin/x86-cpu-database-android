# -*- coding: utf-8 -*-
"""Validate the rebuilt cpus_db: new rows only, plus structural parity with the original."""

import json
from collections import Counter
from pathlib import Path

W = Path(__file__).resolve().parent
orig = json.loads((W / 'payload' / 'cpus_db').read_text(encoding='utf-8'))
new = json.loads((W / 'payload' / 'cpus_db.new').read_text(encoding='utf-8'))

errors, warns = [], []
MAX0 = {t: max(int(r['id']) for r in orig[t]) for t in orig}

# 1. structure parity ---------------------------------------------------------
if list(orig.keys()) != list(new.keys()):
    errors.append('top-level key order changed')
for t in orig:
    ko = list(orig[t][0].keys())
    bad = [i for i, r in enumerate(new[t]) if list(r.keys()) != ko]
    if bad:
        errors.append(f'{t}: {len(bad)} rows with different key order')

# 2. new rows only ------------------------------------------------------------
for v in ('intel', 'amd'):
    prods = {p['id'] for p in new[f'{v}_products']}
    series = {s['id']: s for s in new[f'{v}_series']}
    new_prods = [p for p in new[f'{v}_products'] if int(p['id']) > MAX0[f'{v}_products']]
    new_series = [s for s in new[f'{v}_series'] if int(s['id']) > MAX0[f'{v}_series']]
    new_cpu = [c for c in new[f'{v}_cpu'] if int(c['id']) > MAX0[f'{v}_cpu']]
    new_data = [d for d in new[f'{v}_cpu_data'] if int(d['id']) > MAX0[f'{v}_cpu_data']]

    for p in new_prods:
        if p['type'] not in ('dk', 'mb', 'sv', 'ed', 'cs'):
            errors.append(f'{v} product {p["id"]} bad type {p["type"]}')
    for s in new_series:
        if s['id_product_family'] not in prods:
            errors.append(f'{v} serie {s["id"]} -> missing product {s["id_product_family"]}')
    for c in new_cpu:
        if c['id_serie'] not in series:
            errors.append(f'{v} cpu {c["name"]} -> missing serie')
    for d in new_data:
        if d['id_cpu'] not in {c['id'] for c in new_cpu}:
            errors.append(f'{v} data {d["name"]} -> missing cpu {d["id_cpu"]}')

    by_cpu = Counter(d['id_cpu'] for d in new_data)
    for c in new_cpu:
        if by_cpu[c['id']] != 1:
            errors.append(f'{v} new cpu {c["name"]} has {by_cpu[c["id"]]} data rows')

    names = Counter(c['name'] for c in new_cpu)
    dup = [n for n, k in names.items() if k > 1]
    if dup:
        errors.append(f'{v} duplicate new names: {dup}')

    for c in new_cpu:
        for f in ('launch', 'cores', 'core_clk', 'core_clk_max'):
            if not str(c[f]).isdigit():
                errors.append(f'{v} {c["name"]} bad {f}={c[f]!r}')
        if not 2018 <= int(str(c['launch'])[:4]) <= 2027:
            errors.append(f'{v} {c["name"]} launch outside 2018-2027: {c["launch"]}')
        if int(c['core_clk_max']) < int(c['core_clk']):
            errors.append(f'{v} {c["name"]} boost < base')

    for d in new_data:
        for f, lo, hi in (('cores', 1, 256), ('threads', 1, 512),
                          ('cache_l3', 0, 1200000), ('cache_l2', 0, 300000),
                          ('cache_l1_inst', 0, 20000), ('cache_l1_data', 0, 20000),
                          ('tdp', 1, 600), ('mem_channels', 1, 16),
                          ('pcie_lanes', 0, 200), ('fab', 1, 250)):
            val = d.get(f)
            if val is None:
                errors.append(f'{v} {d["name"]} null {f}')
                continue
            try:
                iv = float(val)
            except (TypeError, ValueError):
                errors.append(f'{v} {d["name"]} non numeric {f}={val!r}')
                continue
            if not lo <= iv <= hi:
                errors.append(f'{v} {d["name"]} {f}={val} out of range')
        if not d.get('socket'):
            errors.append(f'{v} {d["name"]} empty socket')
        if not d.get('core_name'):
            errors.append(f'{v} {d["name"]} empty core_name')
        if not d.get('mem_type'):
            errors.append(f'{v} {d["name"]} empty mem_type')
        if d['cache_l3'] and int(d['cache_l3']) < 1024:
            warns.append(f'{v} {d["name"]} suspicious L3={d["cache_l3"]}')

# 3. summary ------------------------------------------------------------------
print('table                    before   after   added')
for t in ('intel_products', 'intel_series', 'intel_cpu', 'intel_cpu_data',
          'amd_products', 'amd_series', 'amd_cpu', 'amd_cpu_data'):
    print(f'{t:22} {len(orig[t]):7} {len(new[t]):7} {len(new[t]) - len(orig[t]):6}')

print()
print('launch year distribution of new CPUs:')
years = Counter(str(c['launch'])[:4] for v in ('intel', 'amd')
                for c in new[f'{v}_cpu'] if int(c['id']) > MAX0[f'{v}_cpu'])
for y in sorted(years):
    print(f'  {y}: {years[y]}')

print()
print(f'ERRORS: {len(errors)}')
for e in errors[:30]:
    print('  -', e)
print(f'WARNINGS: {len(warns)}')
for w in warns[:10]:
    print('  -', w)
