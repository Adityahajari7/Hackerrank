#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    if n == 1 or n== 2 or n==4 or n==7:
      print "-1"
    elif  n%3 == 0:
      print "5"*n
   
    elif n%3 == 2:
      print "5"*(n-5)+"3"*5
    elif n%3 ==  1:
      print "5"*(n-10)+"3"*10
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     