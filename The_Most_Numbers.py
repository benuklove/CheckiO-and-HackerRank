"""

  Created on 1/4/2017 by Ben

  benuklove@gmail.com
  
  Solution to CheckiO's elementary problem "The Most Numbers"

"""


def checkio(*args):
    if not args:
        difference = 0
    else:
        mini, maxi = args[0], args[0]
        for number in args:
            if number < mini:
                mini = number
            if number > maxi:
                maxi = number
        difference = maxi - mini
    return difference

print(checkio(7, 3, 2, 10.2))
print("then")
print(checkio())
