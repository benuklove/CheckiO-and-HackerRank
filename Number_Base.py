"""

  Created on 1/5/2017 by Ben

  benuklove@gmail.com
  
  Solution to CheckiO's simple problem "Number Base"

"""


def checkio(str_number, radix):
    try:
        x = int(str_number, radix)
        pass
    except ValueError:
        x = -1
    return x

print(checkio("AF", 16))
print(checkio("101", 2))
print(checkio("101", 5))
print(checkio("Z", 36))
print(checkio("AB", 10))
