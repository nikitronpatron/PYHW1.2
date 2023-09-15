# Напишите программу, которая получает целое число и возвращает 
# его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

num = int(input("Enter num: "))
num_ = num
hex_ = ''
while num > 0:
    if num % 16 < 10:
        hex_ = str(num % 16) + hex_
    elif num % 16 == 10:
        hex_ = str('A') + hex_
    elif num % 16 == 11:
        hex_ = str('B') + hex_
    elif num % 16 == 12:
        hex_ = str('C') + hex_
    elif num % 16 == 13:
        hex_ = str('D') + hex_
    elif num % 16 == 14:
        hex_ = str('E') + hex_
    elif num % 16 == 15:
        hex_ = str('F') + hex_
    num //= 16
print(hex_)
print(hex(num_))