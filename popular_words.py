def popular_words(text, words):

    # remove punctuation with regex
    import re
    clean_string = re.sub(r"[^\w\s']", '', text)

    # put cleaned string of text into a list, one word for each element
    clean_string = clean_string.split()

    # initialize a dictionary from words as keys, zeroes as values
    result = dict.fromkeys(words, 0)

    # loop over both iterators at O(n^2) to find matches
    for word in words:
        for i in clean_string:
            if word == i.lower():
                result[word] += 1

    return result


print(popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three', 'one']))
