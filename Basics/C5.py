
import codecs
def repeated_xor(text,key):
    t_bytes = str(text).encode('utf-8')
    output = b''
    for i,byte in enumerate(t_bytes):
        # print(i,char)
        output += bytes([byte^key[i%len(key)]])
    return output
if __name__== '__main__':
    text= ["Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"]

    print(repeated_xor(text[0],b'ICE').hex())
