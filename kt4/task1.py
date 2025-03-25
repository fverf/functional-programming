#функция gen-if-even-x которая создает замыкание с аргументом x

def gen_if_even_x(x):
    return lambda func: func(x) if x % 2 == 0 else x
def increment(x):
    return x + 1

even_inc = gen_if_even_x(4)
print(even_inc(increment))
odd_inc = gen_if_even_x(3)
print(odd_inc(increment))