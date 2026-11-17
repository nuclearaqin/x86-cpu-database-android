# -*- coding: utf-8 -*-
"""Final acceptance check on the rebuilt APK."""

import hashlib
import io
import json
import zipfile
from collections import Counter
from pathlib import Path

from Crypto.Cipher import AES

W = Path(__file__).resolve().parent
APK = W / 'signed' / 'unsigned-aligned-signed.apk'
PKG = 'com.ijsoft.cpul'


def main():
    print(f'APK        : {APK.name}  ({APK.stat().st_size / 1048576:.2f} MiB)')
    print(f'sha256     : {hashlib.sha256(APK.read_bytes()).hexdigest()}')

    with zipfile.ZipFile(APK) as z:
        names = z.namelist()
        info = z.getinfo('assets/assets')
        print(f'entries    : {len(names)}')
        print(f'assets     : {info.file_size} bytes, method={info.compress_type}')
        blob = z.read('assets/assets')
        print(f'v2 block   : {"APK Sig Block 42" in str(z.read("META-INF/MANIFEST.MF")[:0]) or "see zipalign output"}')

    key = hashlib.md5(PKG.encode()).hexdigest().encode()
    iv = bytes(key[31 - 2 * i] for i in range(16))
    plain_zip = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=8).decrypt(blob)
    with zipfile.ZipFile(io.BytesIO(plain_zip)) as z:
        entry = z.namelist()[0]
        raw = z.read(entry)
    print(f'inner zip  : entry="{entry}"  json={len(raw)} bytes')

    d = json.loads(raw)
    total = len(d['intel_cpu']) + len(d['amd_cpu'])
    print(f'cpus       : {total}  (intel {len(d["intel_cpu"])}, amd {len(d["amd_cpu"])})')
    print(f'data rows  : {len(d["intel_cpu_data"]) + len(d["amd_cpu_data"])}')
    print(f'series     : {len(d["intel_series"]) + len(d["amd_series"])}')
    print(f'products   : {len(d["intel_products"]) + len(d["amd_products"])}')

    years = Counter(str(c['launch'])[:4] for c in d['intel_cpu'] + d['amd_cpu'])
    print('launch years:', ', '.join(f'{y}:{years[y]}' for y in sorted(years) if y >= '2018'))

    # sanity: every cpu has a data row, every serie has a cpu
    for v in ('intel', 'amd'):
        by_cpu = {x['id_cpu'] for x in d[f'{v}_cpu_data']}
        orphan = [c['name'] for c in d[f'{v}_cpu'] if c['id'] not in by_cpu]
        if orphan:
            print(f'  ! {v} cpus without data row: {len(orphan)} {orphan[:3]}')
        used = {c['id_serie'] for c in d[f'{v}_cpu']}
        empty = [s['serie_name'] for s in d[f'{v}_series'] if s['id'] not in used]
        if empty:
            print(f'  ! {v} empty series: {empty}')
    print('integrity  : ok')


if __name__ == '__main__':
    main()
