"""

  Created on 12/18/2016 by Ben

  benuklove@gmail.com
  
  HR - Circular Array Rotation

"""

#!/bin/python3

import sys


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

def rotate(arr):
    arr.insert(0, arr[n-1])
    arr.pop()
    return arr

for times in range(k):
    rotate(a)

for a0 in range(q):
    m = int(input().strip())
    print(a[m])
