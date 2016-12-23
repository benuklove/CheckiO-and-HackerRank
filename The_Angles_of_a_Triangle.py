"""

  Created on 12/19/2016 by Ben

  benuklove@gmail.com
  
  Solution to The Angles of a Triangle on CheckiO.
  Given the three sides of a triangle, output a sorted list of angles.
  Output a list of zeroes if lengths cannot form a triangle.

"""

from math import acos, degrees


# Using the Law of Cosines, find the angles
def checkio(a, b, c):

    angles = []

    while True:
        try:
            bigC = round(degrees(acos((c ** 2 - a ** 2 - b ** 2) / (-2 * a * b))))
            break
        except ValueError:
            bigC = 0
            break
    angles.append(bigC)

    while True:
        try:
            bigA = round(degrees(acos((a ** 2 - b ** 2 - c ** 2) / (-2 * b * c))))
            break
        except ValueError:
            bigA = 0
            break
    angles.append(bigA)

    while True:
        try:
            bigB = round(degrees(acos((b ** 2 - a ** 2 - c ** 2) / (-2 * a * c))))
            break
        except ValueError:
            bigB = 0
            break
    angles.append(bigB)
    angles.sort()

    # test for degeneration
    if a + b <= c or b + c <= a or c + a <= b:
        angles = [0, 0, 0]

    return angles

print(checkio(10, 20, 30))
