#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/07

@summary: 

@author: huxiufeng
'''
import Image
import ImageDraw

def getpostion(i):
    row = 0
    col = 0
    

def getdata(orifile,outfile):
    im = Image.open(orifile, 'r')
    ot = Image.new('RGB',(100,100), (0,0,0,))
    dw = ImageDraw.Draw(im)
    print im.size
    
    for i in xrange(10000) :
        d = im.getpixel((i,0))
        ps = getpostion(i)
        dw.draw(ps, d)
        
    
#----------------------It is a split line--------------------------------------
def main():
    orifile = r'res/wire.png'
    outfile = r'res/p14.png'
    getdata(orifile,outfile)
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"