#лямбда-функция для возведения в куб и передача в if-even

ifeven = lambda func, x: func(x) if x % 2 == 0 else None
result = ifeven(lambda x: x ** 3, 6)
print(result)
