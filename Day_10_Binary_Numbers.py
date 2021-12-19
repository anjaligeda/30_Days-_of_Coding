#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    temp=0
s=""
rem=0
while(n>0):
      temp=int(n/2)
      rem=n%2
      s=s+str(rem)
      n=temp
#forfind consecutive no of 1's in binary representation....s
length=0
count=0
one="1"
for i in range(len(s)):
      #to check the one 
    if(s[i]==one):
        count+=1
        #to update the length..
        if(count>length):
              length=count
    else:
           count=0
#print the no of one's in binary representation...
print(length)      
  
  '''INPUT:
  5
  OUTPUT:
  1'''
