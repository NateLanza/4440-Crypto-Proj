#!/usr/bin/env python3
# coding: iso-8859-1
   
MSG = bytes(r"""�:��[�oQ_aA�]�_�݊�����9��Z����N�kL��W�@NC!J
M<&5�����Svc�.�5/����K���L�
� �_���x��	���:B���cseD�h��3D��
""", "iso-8859-1")
from hashlib import sha256
hex_d = sha256(MSG).hexdigest()
if hex_d == "03fcc222def74f23de1dc5e8463ccbe8d95121d232e50e1a4602e6aba31ae93d":
    print("I come in peace.")
elif hex_d == "fc130dd1499b77dcf133fd1566a667d4e6ef5f24f47d5c5fe4248a55d736976f":
    print("Prepare to be destroyed!")