"""

  Created on 1/4/2017 by Ben

  benuklove@gmail.com
  
  Solution to CheckiO's Elementary problem, "Three Words"

"""


def checkio(words):
    wordlist = words.split(" ")
    print(wordlist)
    count = 0
    for word in wordlist:
        if word.isalpha():
            count += 1
            if count == 3:
                break
        else:
            count = 0
    if count == 3:
        print("truebeee")
        return True
    else:
        print("falseee")
        return False

checkio("hello 22 hello dude okay")
