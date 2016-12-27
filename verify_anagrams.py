"""

  Created on 12/26/2016 by Ben

  benuklove@gmail.com
  
  Solution to Verify Anagrams on CheckiO.
  Function that takes in two words to see if they are anagrams of each other.
  Also times it.

"""


def verify_anagrams(first_word, second_word):
    first_word = first_word.lower().replace(" ", "")
    second_word = second_word.lower().replace(" ", "")
    if len(first_word) != len(second_word):
        return False
    flag = 0
    for letter in first_word:
        if first_word.count(letter) == second_word.count(letter):
            continue
        else:
            flag = 1
    if flag == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    from timeit import Timer
    # tt = Timer(lambda: verify_anagrams("Programming", "Gram Ring Mop"))
    tt = Timer(lambda: verify_anagrams("Hello!", "Ole Oh!"))
    print(tt.timeit(number=1))
