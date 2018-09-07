
import codecs
from Crypto.Cipher import AES

with open('C7.txt') as fb:
    data = codecs.decode(bytes(fb.read().encode('utf-8')),'base64')
    key = b'YELLOW SUBMARINE'
    encryp = AES.new(key,AES.MODE_ECB)
    print(encryp.decrypt(data))
