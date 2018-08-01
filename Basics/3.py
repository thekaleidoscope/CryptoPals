import codecs
import binascii
import string
CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}

def english_score(input_bytes):
    score = 0
    for byte in input_bytes:
        score += CHARACTER_FREQ.get(chr(byte).lower(),0)

    return score

def xor(input_bytes, key):
    output = b''
    for char in input_bytes:
        output+= bytes([char^key])
    return output

def test_xor(input_bytes):
    high_score=-1
    res={
    'key':None,
    'element':None,
    'score':0
    }
    for i in range(256):

        element= xor(input_bytes,i)
        score=english_score(element)
        # print(element,score)

        if score >   res['score']:
            res['key']=i
            res['element'] = element
            res['score']=score
    return res

if __name__== '__main__':
    a= input()
    # print(string.ascii_letters)
    a=codecs.decode(a,'hex')

    res=test_xor(a)
    print(res)
