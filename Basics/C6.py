from itertools import combinations
import codecs
import C3
import C5
from base64 import b64decode


def hamming_dist(x,y):
    dist=0
    for a,b in zip(x,y):
        dif=a^b
        dist += sum( [1 for bit in bin(dif) if bit=='1'])
    return dist

def find_key_length(input1):
    norm_distances= {}
    for l in range(2,41):

        block_possibilities= [input1[i : i+l ] for i in range(0,len(input1),l)][:4]

        pairs= combinations(block_possibilities,2)
        dist=0
        for (x,y) in pairs:
            dist+= hamming_dist(x,y)
        dist/=6
        norm_dist= dist / l
        norm_distances[l]=norm_dist
    keys=sorted(norm_distances,key=norm_distances.get)[:5]
    # print(keys)
    return keys

def attempt_key_search(input1):
    text = []
    keys = find_key_length(input1)
    for key_len in keys:
        key=b''
        for i in range(key_len):
            block = b''
            for index in range(i,len(input1),key_len):
                block+=bytes([input1[index]])
            key+=bytes([C3.test_xor(block)['key']])
        text.append((C5.repeated_xor(input1,key),key))

    max=()
    h_score=-1
    for a in text:
        # print(a[0])
        s=C3.english_score(a[0])
        if(s>h_score):
            h_score=s
            max=a
    print(max[1].decode())
    # print(max[0].decode().rstrip())

    # print(len(text))


if __name__ == '__main__':
    # d=hamming_dist(b'this is a test', b'wokka wokka!!!')
    # print(d)
    assert hamming_dist(b'this is a test', b'wokka wokka!!!') == 37

    with open('C6.txt') as fb:
        data = codecs.decode(bytes(fb.read().encode('utf-8')),'base64')

    attempt_key_search(data)
