# 2 - Напишите программу, которая принимает на вход число N
#  и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

numbers = []
print("Введите целое положительное число 'N'")
number = (input())
if number.isdigit() == True:
    number = int(number)
    if number < 0:
        print('вы ввели отрицательное число')
    else:
        i = 1
        factorial = 1
        while i <= number:
            factorial *= i
            numbers.append(factorial)
            i = i + 1
        print("набор произведений чисел от 1 до N : ", numbers)
else:
    print('вы ввели не число')
