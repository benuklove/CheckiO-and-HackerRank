from timeit import timeit


def best_stock(data):
    maxx = 0
    best = ""
    for key, value in data.items():
        if value > maxx:
            maxx = value
            best = key
    return best


def slower_better_stock(data):
    # your code here
    return max(data, key=data.get)


# print(timeit(best_stock({
#         'CAC': 10.0,
#         'ATX': 390.2,
#         'WIG': 1.2
#     }), number=1000))


stocks = {
    'CAC': 10.0,
    'ATX': 390.2,
    'WIG': 1.2
}

if __name__ == "__main__":
    print(timeit("best_stock(stocks)",
                 "from __main__ import best_stock, stocks",
                 number=1000000),
          timeit("slower_better_stock(stocks)",
                 "from __main__ import slower_better_stock, stocks",
                 number=1000000)
          )
