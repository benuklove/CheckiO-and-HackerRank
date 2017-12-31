def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    longest = 0
    if line:
        current_count = 0
        line = list(enumerate(line))
        for i in line:
            if i[0] > 0:
                if i[1] == line[line.index(i) - 1][1]:
                    current_count += 1
                    if current_count > longest:
                        longest = current_count
                else:
                    current_count = 0

        longest += 1
    print(longest)
    return longest


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')