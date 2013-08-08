#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/05

@summary: 

@author: huxiufeng
'''


#----------------------It is a split line--------------------------------------

def isph(ch):
    if ord(ch) <= ord('z') and ord(ch) >= ord('a') :
        return True
    if ord(ch) <= ord('Z') and ord(ch) >= ord('A') :
        return True
    return False

def tran(ch):
    if ch == 'y':
        return 'a'
    elif ch =='z':
        return 'b'
    else:
        return chr(ord(ch)+2)
 

def transword(ori):
    #ori = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
    des = ''
    for i in ori :
        if isph(i):
            i = tran(i)
        des += i
    print des
    return des
            

def main():
    ori = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
    transword(ori)
    ori  = 'map'
    transword(ori)
    
            
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"