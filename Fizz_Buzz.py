"""

  Created on 12/31/2016 by Ben

  benuklove@gmail.com
  
  Fizz Buzz.  Just doing it.  ^_^
  From CheckiO.

"""


def checkio(number):
    if number % 3 == 0 and number % 5 == 0:
        output = "Fizz Buzz"
    elif number % 3 == 0:
        output = "Fizz"
    elif number % 5 == 0:
        output = "Buzz"
    else:
        output = str(number)
    return output

print(checkio(15))
print(checkio(6))
print(checkio(5))
print(checkio(7))

if __name__ == '__main__':
    from timeit import Timer
    tt = Timer(lambda: checkio(15))
    print(tt.timeit(number=1))
