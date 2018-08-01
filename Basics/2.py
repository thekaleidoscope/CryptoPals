import codecs
def hex_decode(base):
    return codecs.decode(base,'hex')
def xor(a,b):
    a= bytearray.fromhex(a)
    b= bytearray.fromhex(b)
    k=[p^q for p,q in zip(a,b)]
    print(a,b,k)

    # print( codecs.encode(a^b,'hex'))

if __name__ == '__main__':
    a,b=input().split()
    print(hex(int(a,16)^int(b,16)))
