import C3
import codecs

if __name__=='__main__':
    with open('C4.txt') as fb:
        high_score =0
        high_res = {}
        for  line in fb:
            # print(line  )
            res = C3.test_xor(codecs.decode(line.strip(),'hex'))
            if(res['score']>high_score):
                high_score=res['score']
                high_res=res
        print(high_res)
