#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
a = []
for i in range(n):
    a.append(arr[n-i-1])
for j in range(n):
    print a[j],