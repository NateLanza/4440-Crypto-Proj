#!/usr/bin/env python3
# coding: iso-8859-1
   
MSG = bytes(r"""«:òÑ[¢oQ_aAê]‘_½ÝŠž½‡‚Ú9†‘ZìýÆÈNëkLÌWÚ@NC!J
M<&5šÊÌú–SvcåŒ.û5/©â‚ï×K­˜LØ
Ã è‹_ˆ×Óxø§	ü´È:BúïcseDÃh¡¶3Dîñ
""", "iso-8859-1")
from hashlib import sha256
hex_d = sha256(MSG).hexdigest()
if hex_d == "03fcc222def74f23de1dc5e8463ccbe8d95121d232e50e1a4602e6aba31ae93d":
    print("I come in peace.")
elif hex_d == "fc130dd1499b77dcf133fd1566a667d4e6ef5f24f47d5c5fe4248a55d736976f":
    print("Prepare to be destroyed!")