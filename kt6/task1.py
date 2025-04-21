#сумма четных чисел с использованием рекурсии
def sum(lst):
    match lst:
        case []:
            return 0
        case [head, *tail]:
            return (head if head % 2 == 0 else 0) + sum(tail)

print(sum([1, 2, 3, 4, 5, 6]))


#обработка вложенных карт через сопоставление
person = {
    "name": "Кукушка",
    "address": {
        "city": "Крыша",
        "zip": "12345"
    }
}
def city(info):
    match info:
        case {"address": {"city": city}}:
            return city
        case _:
            return None

print(city(person))


#примеры сопоставления с несколькими условиями
def describenumber(x):
    match x:
        case int() if x < 0:
            return "отрицательное число"
        case int() if x == 0:
            return "ноль"
        case int() if x > 0:
            return "положительное число"
        case float():
            return "число с плавающей точкой"
        case _:
            return "неизвестное значение"

print(describenumber(-5))
print(describenumber(0))
print(describenumber(3))
print(describenumber(3.14))
print(describenumber("ку"))