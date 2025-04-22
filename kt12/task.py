#композиция строка, с верхний регистр, первые 3 символа


compose_upper3 = lambda s: s.upper()[:3]
print(compose_upper3("ку"))


#фильтрация отрицательных, умножение на 2, сумма
process_numbers = lambda nums: sum(map(lambda x: x * 2, filter(lambda x: x >= 0, nums)))
print(process_numbers([1, -2, 3, -4, 5]))



# строка, слова, фильтрация по длине > 3, количество
count_long_words = lambda s: len(list(filter(lambda w: len(w) > 3, s.split())))
print(count_long_words("ку куку кууу ку куу ку ку ку"))