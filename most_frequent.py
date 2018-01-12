def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # Build a dict of unique items with set, sum occurrences for values
    d = {}
    for key in set(data):
        d[key] = sum(1 for x in data if x == key)
    # Find key of max value through lambda of values
    max_key = max(d, key=lambda k: d[k])

    return max_key


most_frequent(['a', 'b', 'c', 'a', 'b', 'a'])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
