#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/15

@summary: 

@author: huxiufeng
'''
import Image

def ptimg(filename):
    im = Image.open(filename)
    
    rows = im.size[0]
    cols = im.size[1]
    
    for i in xrange(rows):
        isequal = False
        bfr = -1
        for j in xrange(cols):
            now = im.getpixel((i,j))
            if bfr == -1:
                bfr = now
                continue
            if now == bfr:
                isequal = True
            bfr = now
            if isequal:
                print now,
        print '\n'
    

#----------------------It is a split line--------------------------------------

def main():
    filename = r'res/mozart.gif'
    ptimg(filename)
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"