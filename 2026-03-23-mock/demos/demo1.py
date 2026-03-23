def f1():
    return "f1"

def f2():
    return "f2"

print(f1())

# f1 is a reference to a function
f1 = f2
print(f1())
