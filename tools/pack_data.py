# -*- coding: utf-8 -*-
"""Repack cpus_db -> zip -> AES-256-CFB8, reproducing assets/assets byte layout."""

import hashlib
import io
import zipfile
from pathlib import Path

from Crypto.Cipher import AES

W = Path(__file__).resolve().parent
SRC_JSON = W / 'payload' / 'cpus_db.new'
OUT_ZIP = W / 'payload' / 'cpus_db.zip'
OUT_ENC = W / 'assets_new.bin'
PKG = 'com.ijsoft.cpul'


def derive():
    key = hashlib.md5(PKG.encode()).hexdigest().encode()
    iv = bytes(key[31 - 2 * i] for i in range(16))
    return key, iv


def make_zip(dst, name, payload: bytes):
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        info = zipfile.ZipInfo(name, date_time=(2018, 11, 16, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        z.writestr(info, payload)


def main():
    raw = SRC_JSON.read_bytes()
    make_zip(OUT_ZIP, 'cpus_db', raw)
    zip_bytes = OUT_ZIP.read_bytes()

    key, iv = derive()
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=8)
    enc = cipher.encrypt(zip_bytes)
    OUT_ENC.write_bytes(enc)

    print(f'json   : {len(raw):>9} bytes')
    print(f'zip    : {len(zip_bytes):>9} bytes  ({len(zip_bytes) / len(raw) * 100:.1f}%)')
    print(f'enc    : {len(enc):>9} bytes  -> {OUT_ENC}')

    # ---- round trip ------------------------------------------------------
    back = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=8).decrypt(enc)
    assert back == zip_bytes, 'decrypt mismatch'
    with zipfile.ZipFile(io.BytesIO(back)) as z:
        names = z.namelist()
        assert names == ['cpus_db'], names
        plain = z.read('cpus_db')
    assert plain == raw, 'zip payload mismatch'
    print(f'round trip OK: {names}, {len(plain)} bytes payload')


if __name__ == '__main__':
    main()
