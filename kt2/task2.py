#лямба вместо let

double_double = lambda x: (lambda dubs: dubs * 2)(x * 2)

print(double_double(3))
print(double_double(5))

