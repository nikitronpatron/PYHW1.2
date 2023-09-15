# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

a = input("Enter dec1: ")
b = input("Enter dec2: ")
a = a.split('/')
b = b.split('/')
c, d, e, f = a[0], a[1], b[0], b[1]

if a[1] == b[1]:
    print(f'{int(a[0]) + int(b[0])}/{a[1]}')
else:
    a[0] = int(a[0]) * int(b[1])
    b[0] = int(b[0]) * int(a[1])
    a[1] = int(a[1]) * int(b[1])
    print(f'sum: {a[0] + b[0]}/{a[1]}')
c = int(c) * int(e)
d = int(d) * int(f)
print(f'mult: {c}/{d}')