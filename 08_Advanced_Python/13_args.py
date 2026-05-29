def sum(*args):

    # args will be a tuple.

    total = 0
    for item in args:
        total += item
    return total


print(sum(8523,6543,4))