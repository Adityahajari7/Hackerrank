# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import math
t = int(raw_input().strip())
for a0 in xrange(t):
    k,n = raw_input().strip().split(' ')
    k,n = [int(k),int(n)]

    if math.sqrt(k)%1==0:
        print int(math.sqrt(n))-int(math.sqrt(k))+1
    else :
        print int(math.sqrt(n))-int(math.sqrt(k)) 
        