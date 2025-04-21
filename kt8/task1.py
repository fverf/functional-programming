#проверка наличия элемента в списке с filter и count
def contains(lst, value):
    return len(list(filter(lambda x: x == value, lst))) > 0

print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 5))


#расширенная проверка палиндрома (без пробелов и регистра)
def is_palindrom(s):
    clean = ''.join(filter(str.isalnum, map(str.lower, s)))
    return clean == clean[::-1]

print(is_palindrom("кукушка кукушонку подарила капюшонку"))  # True
print(is_palindrom("не подарила"))


#гармоническая сумма с ленивыми вычислениями
def harmonic(n):
    return sum(1 / i for i in range(2, n + 2))
print(harmonic(5))