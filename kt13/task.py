#чистая функция, принимает строку и возвращает ее длину
def string_length(s):
    return len(s)

print(string_length("ляляляля"))

#из нечистой функции в чистую
count = 0

def impure_increment():
    global count
    count += 1
    return count
print(impure_increment())

def pure_increment(n):
    return n + 1
print(pure_increment(0))

#обработка списка чисел с помощью чистых функций
def process_numbers(nums):
    return list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))

print(process_numbers([1, 2, 3, 4, 5, 6]))
