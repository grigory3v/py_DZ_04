# 3-Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между максимальным
#   и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

list_1 = [1.1, 1.2, 3.1, 5.17, 10.02]
list_2 = [4.07, 5.1, 8.2444, 6.98]


def List(incoming_list):
    """Функция, которая найдёт разницу между максимальным 
    и минимальным значением дробной части элементов списка."""

    min_value_fractional_part_elements = incoming_list[0] % 1
    max_value_fractional_part_elements = incoming_list[0] % 1

    for i in range(1, len(incoming_list)):

        if incoming_list[i] % 1 > max_value_fractional_part_elements:
            max_value_fractional_part_elements = incoming_list[i] % 1
        elif incoming_list[i] % 1 < min_value_fractional_part_elements:
            min_value_fractional_part_elements = incoming_list[i] % 1

    difference_between_elements = max_value_fractional_part_elements - \
        min_value_fractional_part_elements
    return round(difference_between_elements, 2)


print('Разница между максимальным и минимальным значением дробной части элементов list_1 = ', List(list_1))
print('Разница между максимальным и минимальным значением дробной части элементов list_2 = ', List(list_2))
