# 5-Задайте число.
# Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,-13, -8, 5, −3, -2, −1, -1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

print ("Задайте число :")
number = int(input())
if number > 0:
    list = []
    fib0 = 0
    fib1 = -1
    fib2 = 1

    list.append(fib0)
    list.append(fib1)
    list.append(fib1)
    list.append(fib2)
    list.append(fib2)

    def Number_fib(fib1, fib2):
        for i in range(2, number):
            fib = fib1 + fib2
            fib1 = fib2
            fib2 = fib
            list.append(fib)

    Number_fib(fib1, fib1)
    Number_fib(fib2, fib2)
    list.sort()
    print(list)

else:
    print("Введите положительное число")
