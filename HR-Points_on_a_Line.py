"""

  Created on 12/18/2016 by Ben

  benuklove@gmail.com
  
  HR - Points on a Line

"""

#!/bin/python3

import sys

xarr = []
yarr = []

n = int(input().strip())
for a0 in range(n):
    x,y = input().strip().split(' ')
    x,y = [int(x),int(y)]
    xarr.append(x)
    yarr.append(y)

xflag = 0
for number in range(1, len(xarr)):
    if xarr[0] != xarr[number]:
        xflag = 1
yflag = 0
for number in range(1, len(yarr)):
    if yarr[0] != yarr[number]:
        yflag = 1

if xflag == 0 or yflag == 0:
    print("YES")
else:
    print("NO")
