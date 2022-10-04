# 1 - Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


print("Введите число :")


def dividers(number):
    while number > 1:
        i = 2
        while i < 10:
            if number % i == 0:
                print(i, end=' ')
                number = int(number / i)
                break
            i += 1
        if number <= 1:
            break
    


dividers(number=int(input()))
