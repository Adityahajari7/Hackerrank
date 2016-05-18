#!/bin/python

import sys
a = []
x = 0
n = int(raw_input().strip())
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)
   x = x + a_temp[a_i]- a_temp[2-a_i]
print abs(x)