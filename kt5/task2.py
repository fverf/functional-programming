#4. поиск максимального элемента
from functools import reduce

find_max = lambda lst: reduce(max, lst)
print(find_max([1, 5, 3, 9, 2]))


#5. фильтрация чeтных чисел
filter_even = lambda numbers: list(filter(lambda x: x % 2 == 0, numbers))
print(filter_even([1, 2, 3, 4, 5]))


#6. объединение двух словарей
merge_maps = lambda d1, d2: {**d1, **d2}
print(merge_maps({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))

