#функция которая принимает список чисел и возвращает список их квадратов

squar = lambda nums: list(map(lambda x: x ** 2, nums))
num = [1, 2, 3, 4, 5]
print(squar(num))