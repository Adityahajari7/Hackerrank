#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    x = 0
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    for i in range(n):
        if a[i] <= 0:
            x = x+1
        else :
            x=x
    
    if k > x:
        print "YES"
    else: 
        print "NO"   
