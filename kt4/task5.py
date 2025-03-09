#функция которая возвращает частично примененную функцию для возведения в степень

def power(base):
    return lambda exponent: base ** exponent

square = power(2)
print(square(3))