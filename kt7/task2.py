#2. удаление всех четных чисел из списка
remove_even = lambda lst: list(filter(lambda x: x % 2 != 0, lst))
print(remove_even([1, 2, 3, 4, 5, 6]))


#3. сумма всех чисел во вложенном списке
def sum_nested(lst):
    match lst:
        case []:
            return 0
        case [head, *tail]:
            return (sum_nested(head) if isinstance(head, list) else head) + sum_nested(tail)

print(sum_nested([1, [2, 3], [4, [5]], 6]))


#4.хвостовая рекурсия для суммы элементов списка
def sum_tail(lst, acc=0):
    match lst:
        case []:
            return acc
        case [head, *tail]:
            return sum_tail(tail, acc + head)

print(sum_tail([1, 2, 3, 4]))
