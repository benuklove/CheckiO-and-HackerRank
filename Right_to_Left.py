"""

  Created on 1/4/2017 by Ben

  benuklove@gmail.com
  
  Solution to CheckiO's elementary problem, "Right to Left"

"""


def left_join(phrases):
    """
            Join strings and replace "right" to "left"
    """
    new_phrase = ""
    newphrase_list = []
    for word in phrases:
        new_word = word.replace("right", "left")
        newphrase_list.append(new_word)
        new_phrase = ",".join(newphrase_list)
    return new_phrase

print(left_join(("left", "right", "left", "stop")))
print(left_join(("bright aright", "ok")))
