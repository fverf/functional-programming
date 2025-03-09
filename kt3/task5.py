#замыканиe для умножения на заданное число

def mult(n):
    return lambda x: x * n

mult = mult(2)
print(mult(5))