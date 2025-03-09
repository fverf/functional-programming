#реализация функции overwrite, используя только лямбда-выражения

overwrite = lambda x: (lambda x: print(x) or (lambda x: print(x) or (lambda x: print(x) or (lambda x: print(x)))(4))(3))(2)

overwrite(1)