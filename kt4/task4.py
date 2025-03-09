#binary-partial принимает бинарную функцию и один ее аргумент

def binary_partial(func, arg1):
    return lambda arg2: func(arg1, arg2)
def add(a, b):
    return a + b

add_to_5 = binary_partial(add, 5)
print(add_to_5(3))