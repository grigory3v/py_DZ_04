# -*- coding: utf-8 -*-

# 3 - В файле, содержащем фамилии студентов и их оценки,
#  изменить на прописные буквы фамилии тех студентов,
#  которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4
file_new = open("task03_new.txt", "wt", encoding='utf-8')

with open('task03.txt', encoding='utf-8') as file:
    for index, line in enumerate(file):
        for i in range(0, len(line)):
            if index == i:
                for i in line:
                    if i == '5' or i == '4':
                        new_line = str.upper(line)
                        file_new.write(new_line)
                        print(new_line)
                    elif i == '3' or i == '2':
                    # else: почему не отрабатывает просто иначе?
                        file_new.write(line)
                        print(line)
                        break
                break
