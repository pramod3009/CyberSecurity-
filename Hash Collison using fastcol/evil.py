#!/usr/bin/python3
# coding: latin-1
blob = """
                A=���/I������B�ݦ&~�E��%JB�5������̍�k\���=T�m2E׌�G&��'6�+z)��m��!���Q�8����t]��� �_���Ӓ$�C`���{M� `ŷ
�e�&g7#w<f#�"""
from hashlib import sha256
if sha256(blob.encode("latin-1")).hexdigest() == "88f95f77bcbcacd52e3da059ffe5e6efb89853ee70482fd5ae4ed2938d2150bf":
        print("Use SHA-256 instead!")
else:
        print("MD5 is perfectly secure!")

