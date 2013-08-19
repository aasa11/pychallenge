#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/07

@summary: 

@author: huxiufeng
'''
import Image
import ImageDraw

def getloop(i):
    sums = 0
    col = 0
    if i == 0:
        return (0,0,0)
    
    for idx in xrange(0,50):
        if sums < i and sums + (99-2*idx) >= i:
            col = 0
            break
        elif sums < i and sums + 2*(99-2*idx) >= i:
            col = 1
            break
        elif sums < i and sums + 3*(99-2*idx) >= i:
            col = 2
            break
        elif sums < i and sums + 4*(99-2*idx) >= i:
            col = 3
            break
        sums += 4* (99-2*idx)
    return (idx, col, i-sums)
        


def getpostion(i):
    (idx, col, left ) = getloop(i)
    print (idx, col, left)
    if col == 0:
        return (idx+left, idx)
    elif col == 1:
        return (99-idx,idx + left-(99-2*idx))
    elif col ==2 :
        return ( 99-idx-(left- 2*(99-2*idx)), 99-idx)
    else :
        return (idx, 99-idx-(left- 3*(99-2*idx)))
    

def getdata(orifile,outfile):
    im = Image.open(orifile, 'r')
    ot = Image.new('RGB',(100,100), (0,0,0))
    dw = ImageDraw.Draw(ot)
    print im.size
    
    for i in xrange(10000) :
        d = im.getpixel((i,0))
        ps = getpostion(i)
        print "i", i
        print ps
        ot.putpixel(ps, d)
        #dw.draw(ps, d)
        
    ot.save(outfile)
        
    
#----------------------It is a split line--------------------------------------
def main():
    orifile = r'res/wire.png'
    outfile = r'res/p14.png'
    getdata(orifile,outfile)
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"