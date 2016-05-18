#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    r = len(str(n))
    c=0
    for i in range(r):
        y = str(n)[i]
        x=int(y)
        if x==0:
            c=c
        elif n%x==0:
            c=c+1
        else :
            c= c
    print c