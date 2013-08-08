#!/usr/bin/
#coding=gbk
'''
Created on 2013/08/07

@summary: 

@author: huxiufeng
'''
import xmlrpclib

#----------------------It is a split line--------------------------------------

def main():
    sp = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php',
                            allow_none = True )
 
    print sp.system.listMethods()
    
    for md in sp.system.listMethods() :
        print md, sp.system.methodHelp(md)
        
    for md in sp.system.listMethods() :
        print md, sp.system.methodSignature(md)

    print sp.phone('Bert')
    
#----------------------It is a split line--------------------------------------

if __name__ == "__main__":
    main()
    print "It's ok"