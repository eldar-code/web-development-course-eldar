def f1():
    print("--------------")
    print("--------------")
    return 5

def f2():
    yield 1
    yield 2
    yield 3

generator = f2()
print(next(generator))
print(next(generator))
print(next(generator))