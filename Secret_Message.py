"""

  Created on 12/31/2016 by Ben

  benuklove@gmail.com
  
  Solution to CheckiO's "Secret Message" problem.
  Function to take in a text and return concatenated capital letters.

"""


def find_message(text):
    """Find a secret message"""
    output = ""
    for letter in text:
        if letter.isupper():
            output += "".join(letter)
    return output

print(find_message("How are you? Eh, ok. Low or Lower? Ohhh."))
