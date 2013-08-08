#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/06

@summary: 

@author: huxiufeng
'''
import Image


def isalpha(ch):
    if ord(ch) <= ord('z') and ord(ch) >= ord('a') :
        return True
    elif ord(ch) <= ord('Z') and ord(ch) >= ord('A') :
        return True
    elif ord(ch) <= ord('9') and ord(ch) >= ord('0') :
        return True
    elif ch ==' ' or ch == ',' or ch == '. ' or ch ==':':
        return True
    return False

def getdata(lst, i):
    ch = chr(lst[i])
    if isalpha(ch):
        return ch
    return None

def openimg(imgfile):
    im = Image.open(imgfile,'r')
    
    for j in xrange(im.size[1]):
        des = ''
        for i in xrange(im.size[0]):
            ch = getdata(im.getpixel((i,j)), 0)
            if ch is not None:
                des += ch
        print des
    

#----------------------It is a split line--------------------------------------

def main():
    imgfile = r'G:\down\ChrDw\oxygen.png'
    openimg(imgfile)
    
    des = ''
    for i in [105, 110, 116,101, 103,114,105, 116, 121] :
        des +=chr(i)
    print des
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"