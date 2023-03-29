def add(*args):
    s = 0
    for n in args:
        s += n
    return s


print(add(2, 2, 2, 2, 2))
