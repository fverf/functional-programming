#функция которая возвращает замыкание для проверки

def delit(divisor):
    return lambda num: num % divisor == 0
delitby3 = delit(3)

print(delitby3(9))
print(delitby3(10))
