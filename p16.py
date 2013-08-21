#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/15

@summary: 

@author: huxiufeng
'''
import Image

def ptimg(filename, outfile):
    im = Image.open(filename)
    om = Image.new('RGB', (im.size[0],im.size[1]),(255,255,255))
    
    cols = im.size[0]
    rows = im.size[1]
    
    for i in xrange(rows):
        data=[im.getpixel((j,i)) for j in xrange(cols)] 
        for p in xrange(cols):
            if data[p] == 195 :
                new = data[p:] + data[:p]
                break
        for m,x  in enumerate(new):
            om.putpixel((m, i), x)
                
        
        
    om.save(outfile)
    
#    for i in xrange(rows):
#        isequal = False
#        bfr = -1
#        for j in xrange(cols):
#            now = im.getpixel((i,j))
#            if bfr == -1:
#                bfr = now
#                continue
#            if now == bfr:
#                isequal = True
#            bfr = now
#            if isequal:
#                print now,
#        print '\n'
    

#----------------------It is a split line--------------------------------------

def main():
    filename = r'res/m.jpg'
    outfile = r'res/p16.jpg'
    ptimg(filename, outfile)
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"