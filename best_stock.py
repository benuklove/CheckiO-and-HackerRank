def best_stock(data):
    # your code here
    maxx = 0
    best = ""
    for key, value in data.items():
        print(key, ":", value)
        if value > maxx:
            maxx = value
            best = key
    return best


print("Example:")
print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))
