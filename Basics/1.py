import hashlib
import binascii

import codecs

base = input()
print(codecs.encode(codecs.decode(base,'hex'),'base64'))
