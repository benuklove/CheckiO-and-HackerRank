"""

  Created on 12/31/2016 by Ben

  benuklove@gmail.com
  
  Simple array index problem.
  From CheckiO's "Index Power"

"""


def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    if n >= len(array):
        output = -1
    else:
        output = array[n] ** n
    return output

print(index_power([1, 2, 10, 100], 3))
print(index_power([1, 2], 2))
