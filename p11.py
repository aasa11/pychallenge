#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/06

@summary: 

@author: huxiufeng
'''
import Image
import ImageDraw

def getdata(imgfile, imgnew):
    im = Image.open(imgfile)
    
    imnew = Image.new('RGB', (im.size[0],im.size[1]))
    dw = ImageDraw.Draw(imnew)
    
    for i in xrange(im.size[1]) :
        
        for j in xrange(im.size[0]) :
            #print im.getpixel((j, i)),
            if (i %2 == 1) and (j %2 == 1):
                dw.point(((j+1)/2,(i+1)/2), im.getpixel((j, i)))
        #print '\n'
        
    del dw
    imnew.save(imgnew)



#----------------------It is a split line--------------------------------------

def main():
    imgfile = r'res/cave.jpg'
    imnew = r'res/p11.jpg'
    getdata(imgfile, imnew)
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"