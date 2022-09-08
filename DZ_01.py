# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными

# Пример:
# 67.82 -> 23
# 0.56 -> 11

import math

print("Введите вещественное число")
number = float((input()))

number_in_string = str(number)
i = 0
sum = 0
size = len(number_in_string)
while i < size:
    if number_in_string[i] != '.':
        if number_in_string[i] == '-':
            index_number = int(number_in_string[i + 1])
            index_number = index_number * (-1)
            i += 1
        else:
            index_number = int(number_in_string[i])
        sum = sum + index_number
    i = i + 1

print("sum =", sum)
