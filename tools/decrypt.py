#!/usr/bin/env python3
"""Decrypt com.ijsoft.cpul assets database.

Scheme recovered from smali:
  key_string = hex(md5(packageName.toByteArray()))   # 32 ASCII chars
  key        = key_string.getBytes()                 # AES-256 key material
  iv[i]      = key_bytes[31 - 2*i]                   # i in 0..15
  cipher     = AES/CFB8/NoPadding, decrypt
"""
import hashlib
import sys
from pathlib import Path

from Crypto.Cipher import AES

PKG = "com.ijsoft.cpul"


def derive():
    key_str = hashlib.md5(PKG.encode()).hexdigest()
    key = key_str.encode()
    iv = bytes(key[31 - 2 * i] for i in range(16))
    return key, iv


def main(src, dst):
    key, iv = derive()
    print(f"package   : {PKG}")
    print(f"key string: {key.decode()}")
    print(f"iv        : {iv.hex()}")
    data = Path(src).read_bytes()
    print(f"input     : {len(data)} bytes")
    cipher = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=8)
    out = cipher.decrypt(data)
    Path(dst).write_bytes(out)
    print(f"output    : {len(out)} bytes -> {dst}")
    print(f"head hex  : {out[:32].hex()}")
    print(f"head ascii: {out[:32]!r}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
