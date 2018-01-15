def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """

    # Replace everything that's not a letter or apostrophe with a space
    # And remove leading whitespace
    import re
    clean = re.sub(r"[^\w']", ' ', text).lstrip(" ")

    # Pass through the text checking for alpha or '
    # Break when you reach the end of the first word
    word = ""
    i = 0
    while i < len(clean):
        if clean[i].isalpha() or clean[i] == "'":
            word += clean[i]
        else:
            break
        i += 1

    return word


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
