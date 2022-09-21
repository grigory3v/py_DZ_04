# 4- Напишите программу,
# которая будет преобразовывать десятичное число в двоичное.
# Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10


def Number_conversion(numbers):
    string = ""
    while numbers/2 != 0:
        string = str(numbers % 2) + string
        numbers //= 2
    return string


def Number_conversion_recurs(numbers):
    string = ""
    if numbers >= 2:
        Number_conversion_recurs(numbers // 2)
    print(numbers % 2, end='')
    
 
 

 
 


    

print("Введите десятичное число :")
number = int(input())

print("Двоичное число = ", Number_conversion(number))
Number_conversion_recurs(number)