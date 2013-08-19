#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/06

@summary: 

@author: huxiufeng
'''

import zipfile
import re

def unzipfile(filename, startid):
    z = zipfile.ZipFile(filename, 'r')
    des = ''
    r = re.compile(r'(\d*)$')
    
    while True :
        print startid
        strs = z.read('%s.txt'%startid)
        print strs
        rslt = r.findall(strs)
        print rslt
        des +=z.getinfo('%s.txt'%startid).comment
        
        try :
            startid = int(rslt[0])
        except :
            break
    print des

 
#----------------------It is a split line--------------------------------------

def main():
    filepath = r'G:/down/ChrDw/channel.zip'
    startid = r'90052'
    
    unzipfile(filepath, startid)
    
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"