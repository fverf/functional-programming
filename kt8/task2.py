#произведение элементов списка через reduce
from functools import reduce
from functools import partial
import operator

def product(lst):
    return reduce(operator.mul, lst, 1)

print(product([1, 2, 3, 4]))


#преобразование строк в верхний регистр через map
def to_uppercase(strings):
    return list(map(str.upper, strings))
print(to_uppercase(["куку", "кукушке"]))


#вычитание 5
subtract_five = partial(lambda x, y: x - y, y=5)
print(subtract_five(10))
print(subtract_five(3))