#1. функция repeat (бесконечное повторение значения)
from itertools import repeat, islice

repeat_ = lambda x: repeat(x)
print(list(islice(repeat_('a'), 5)))


#2. подпоследовательность
subseq = lambda start, end, seq: list(islice(seq, start, end))
print(subseq(2, 5, range(1, 10)))


#3. находится ли элемент в первой половине
in_first_half = lambda elem, lst: elem in lst[:len(lst)//2]
print(in_first_half(3, [1, 2, 3, 4, 5, 6]))
print(in_first_half(5, [1, 2, 3, 4, 5, 6]))