#map для преобразования списка строк в их длины

strings = ["hello", "world", "lambda", "functions"]
lengths = list(map(lambda s: len(s), strings))
print(lengths)


#функция-замыкание, которая добавляет префикс к строкам

prefix = lambda prefix: lambda s: prefix + s

ky = prefix("куку, ")
print(ky("кукушке"))
print(ky("кукушонку"))


#partial для создания частично примененной функции
from functools import partial

power = lambda base, exponent: base ** exponent
square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))
print(cube(3))