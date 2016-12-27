"""

  Created on 12/26/2016 by Ben

  benuklove@gmail.com
  
  Brute force takes too long.  And by the way, misses edge cases anyway.

"""

# import sys

# params = []
# n = int(input().strip())
# print(n)
# for item in range(n):
#     i, j = input().strip().split(' ')
#     i, j = [int(i), int(j)]
#     print(i, j)
#     params.append([i, j])
# print(params)

params = [[2, 3], [3, 7], [4, 1]]
rect = []

largest = 0
for item in params:
    if item[0] > largest:
        largest = item[0]
for line in range(largest):
    rect.append([0])

for rec in params:
    for row in range(rec[0]):
        if len(rect[row]) >= rec[1]:
            for element in range(rec[1]):
                rect[row][element] += 1
        else:
            for element in range(len(rect[row]), rec[1]):
                rect[row].append(0)
            for element in range(rec[1]):
                rect[row][element] += 1

highest = rect[0][0]

count = 0
for rec in params:
    for element in rec:
        if element == highest:
            count += 1
print(count)
