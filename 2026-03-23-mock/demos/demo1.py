def f1():
    return "f1"

def f2():
    return "f2"

print(f1())

# f1 is a reference to a function
x = f1 # save the address of the original function as x
f1 = f2 # change the address for f1
print(f1())

# how to get back to the original f1
f1 = x # go back to the original address
print(f1())

