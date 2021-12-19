#an hourglass sum
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        sum=0
        tarr=[]
 
      
for i in range(0,4):
    for j in range(0,4):
        for l in range(i,i+3):
            for k in range(j,j+3):
                if l==i+1 and (k==j or k==j+2):
                    continue
                else:
                    sum+=arr[l][k]
        tarr.append(sum)
        sum=0
        print(max(tarr))
        
        '''INPUT:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

OUTPUT:
19
