#1. ленивая последовательность кубов чисел
def cubes():
    n = 0
    while True:
        yield n ** 3
        n += 1

cube_seq = cubes()
print([next(cube_seq) for _ in range(10)])


#2. ленивое генерирование чисел кратных 3 или 5
def multiples_of_3_or_5():
    n = 0
    while True:
        if n % 3 == 0 or n % 5 == 0:
            yield n
        n += 1

multi_seq = multiples_of_3_or_5()
print([next(multi_seq) for _ in range(10)])


#3. ленивый генератор чисел Фибоначчи с начальных значений
def fibonacci(a, b):
    while True:
        yield a
        a, b = b, a + b

fib_seq = fibonacci(1, 1)
print([next(fib_seq) for _ in range(10)])