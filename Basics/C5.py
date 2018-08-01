
import codecs

if __name__== '__main__':
    text= ["Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"]
    def repeated_xor(text):
        t_bytes = text.encode('utf-8')
        output = b''
        key=b"ICE"
        for i,byte in enumerate(t_bytes):
            # print(i,char)
            output += bytes([byte^key[i%len(key)]])
        return output.hex()
    print(repeated_xor(text[0]))
