#каррированная функция умножения четырёх чисел
def multiply(a):
    return lambda b: lambda c: lambda d: a * b * c * d

print(multiply(2)(3)(4)(5))


#каррированная функция добавления суффикса
def add_suffix(suffix):
    return lambda word: word + suffix

add_ing = add_suffix("ка")
print(add_ing("кукуш"))


#каррированная функция разности
def subtract(a):
    return lambda b: a - b

print(subtract(10)(4))