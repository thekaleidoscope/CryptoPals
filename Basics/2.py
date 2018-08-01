
    # print( codecs.encode(a^b,'hex'))

if __name__ == '__main__':
    a,b=input().split()
    print(hex(int(a,16)^int(b,16)))
