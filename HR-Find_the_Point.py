"""

  Created on 1/5/2017 by Ben

  benuklove@gmail.com
  
  HR - Find the Point

"""

n = int(input().strip())
for a0 in range(n):
    px, py, qx, qy = input().strip().split(" ")
    px, py, qx, qy = int(px), int(py), int(qx), int(qy)
    diffx = qx - px
    diffy = qy - py
    rx = qx + diffx
    ry = qy + diffy
    print(rx, ry)
