"""

  Created on 1/5/2017 by Ben

  benuklove@gmail.com
  
  Solution to CheckiO's simple problem "Absolute Sorting"

"""
import operator


def checkio(numbers_array):
    numlist = list(numbers_array)
    abslist = [abs(x) for x in numlist]
    numdict = dict(zip(abslist, numlist))
    sorted_dict = sorted(numdict.items(), key=operator.itemgetter(0))
    output = []
    for item in sorted_dict:
        output.append(item[1])
    return output

print(checkio((-20, -5, 10, 15)))
