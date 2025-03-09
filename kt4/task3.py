#Определите новую функцию binary-partial
#которая принимает бинарную функцию и один её аргумент

def binary(func, arg1):
    return lambda arg2: func(arg1, arg2)

def add(a, b):
    return a + b

add_to_5 = binary(add, 5)
print(add_to_5(3))
