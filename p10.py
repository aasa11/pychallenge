#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/06

@summary: 

@author: huxiufeng
'''


def getnext(data):
    des = ''
    count = 0
    idx = None
    bf = None
    for i in data :
        if bf is None :
            idx = i
            count = 1
            bf = idx
        elif i == bf :
            count += 1
        else :
            des += str(count)
            des += idx
            idx = i
            count = 1
            bf = idx
            
    #all over
    des +=str(count)
    des +=idx
    #print des
    return des
    


#----------------------It is a split line--------------------------------------

def main():
    ori = '1'
    for i in range(30):
        print i+1, 
        ori = getnext(ori)
        print len(ori)
        print ori

    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"