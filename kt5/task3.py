#7.суммирование значений в списке
from functools import reduce

sum_list = lambda lst: reduce(lambda x, y: x + y, lst)
print(sum_list([1, 2, 3, 4]))


#8.уникальные значения из двух списков
unique_from_two = lambda lst1, lst2: set(lst1).union(lst2)
print(unique_from_two([1, 2, 3], [3, 4, 5]))


#9.преобразование строк в длины
map_lengths = lambda strs: list(map(len, strs))
print(map_lengths(['куку', 'всем', 'кукушкам']))