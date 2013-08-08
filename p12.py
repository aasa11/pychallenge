#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/06

@summary: 

@author: huxiufeng
'''
import os

def devidefile(orifile):
    infile = open(orifile, 'rb')
    desfile = []
    for i in xrange(5):
        outf = open('%d.png'%i, 'wb')
        desfile.append(outf)
    
    insize = os.path.getsize(orifile)
        
    for i in xrange(0, insize, 5):
        for j in xrange(5):
            desfile[j].write(infile.read(1))
    infile.close()
    
    for i in xrange(5):
        desfile[j].close()



#----------------------It is a split line--------------------------------------

def main():
    imgfile = r'res/evil2.gfx'
    devidefile(imgfile)
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"