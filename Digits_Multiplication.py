"""

  Created on 1/5/2017 by Ben

  benuklove@gmail.com
  
  Solution to CheckiO's elementary problem "Digits Multiplication"

"""


def checkio(number):
    product = 1
    new_number = number
    while new_number:
        if new_number % 10 != 0:
            product *= new_number % 10
            new_number //= 10
        else:
            new_number //= 10
    return product

print(checkio(123405))
print(checkio(999))
print(checkio(1000))
print(checkio(1111))
print(checkio(123))
