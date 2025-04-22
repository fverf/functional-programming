# числа фибоначчи

def fib(n):
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fib(n - 1) + fib(n - 2)

print(fib(10))

# быстрая версия (fast_fib с аккумуляторами)

def fast_fib(n1, n2, counter):
    while counter > 0:
        n1, n2 = n2, n1 + n2
        counter -= 1
    return n1

print(fast_fib(1, 1, 5))
print(fast_fib(1, 1, 1000))