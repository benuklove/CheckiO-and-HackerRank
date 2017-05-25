"""

  Created on 5/24/2017 by Ben

  benuklove@gmail.com
  
  Different ways to find the maximum value in an array.
  Inspired by an interview question.

"""

# Because I learned C first, I did it something like this in the interview.
# Not very pythonic.

def max_index_C(array):
    index = 0
    max = array[0]
    max_index = 0
    for i in array:
        if i > max:
            max = i
            max_index = index
        index += 1
    return max_index

my_list = [2, 1, 3, 2, 2]
print(max_index_C(my_list))


# Here's an easy way to do it, though I'm not sure how the interviewer
# would interpret my ability to reason through code.

def max_index_easy(array):
    return array.index(max(array))

print(max_index_easy(my_list))


# A cool way to return all indexes of max values with list comprehensions
# and enumerate.

def max_index_enum(array):
    return [x[0] for x in list(enumerate(array)) if x[1] == max(array)]

print(max_index_enum(my_list))


# Another enumerate usage that also uses the 'get' method on the dictionary.

def max_index_get(array):
    return max(dict(enumerate(array)), key=dict(enumerate(array)).get)

print(max_index_get(my_list))

# with generators
