#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/06

@summary: 

@author: huxiufeng
'''

import base64
import bz2

def decodebz2(ori):
    des = bz2.decompress(ori)
    print des
    return des

def decode64(ori):
    des = base64.decodestring(ori)
    print des
    return des


def mins(ori):
    mins = 1000
    for i in ori :
        if mins > int(i):
            mins = int(i)
    print mins
    return mins


def getch(data, offset):
    des = ''
    ori = data.split(',')
    mins(ori)
    print len(ori)
    for i in ori:
        des += chr(int(i)-offset)
    print des 
    return des

#----------------------It is a split line--------------------------------------

def main():
    data = '''179,284,214,311,255,320,281,226,319,224,363,309,339,222,371,225,411,229,404,242,415,252,428,233,428,214,394,207,383,205,390,195,423,192,439,193,442,209,440,215,450,221,457,226,469,202,475,187,494,188,494,169,498,147,491,121,477,136,481,96,471,94,458,98,444,91,420,87,405,92,391,88,376,82,350,79,330,82,314,85,305,90,299,96,290,103,276,110,262,114,225,123,212,125,185,133,138,144,118,160,97,168,87,176,110,180,145,176,153,176,150,182,137,190,126,194,121,198,126,203,151,205,160,195,168,217,169,234,170,260,174,282'''
    
    usr = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pwd = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    
    #desusr = decode64(usr)
    desusr = decodebz2(usr)
    despwd = decodebz2(pwd)
    #getch(data, 79)
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"