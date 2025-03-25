#функция, которая проверяет, четное ли число

def process_number(n):
    if n % 2 == 0:
        return n + 2
    else:
        return 3 * n - 1