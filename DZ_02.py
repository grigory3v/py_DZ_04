# 2-Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]
list_2 = [2, 3, 5, 6]


def List(incoming_list):
    """Функция, которая найдёт произведение пар чисел списка.
    
    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    """

    new_list = []
    for i in range(0, len(incoming_list)//2):
        new_list.append(incoming_list[i] *
                        incoming_list[len(incoming_list) - i - 1])

    if (len(incoming_list) % 2) != 0:
        average_index = len(incoming_list)//2
        new_list.append(incoming_list[average_index]
                        * incoming_list[average_index])

    return new_list


print('Произведение пар чисел списка = ', List(list))

print('Произведение пар чисел списка = ', List(list_2))
