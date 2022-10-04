# -*- coding: utf-8 -*-

# 4- Шифр Цезаря - это способ шифрования,
# где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо.
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
#  а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

alphabets = []
for i in range(97, 123):
    alphabets.append(chr(i))
print(alphabets)


def Shifr(word):
    word_new = (" ")
    index_alphabets = 26
    print("Введите ключ шифрования :")
    number = int(input())
    for j in range(0, len(word)):
        for l in range(0, len(alphabets)):
            if word[j] == alphabets[l]:
                index_number = 0
                if number > 0:
                    index_number = number + l
                    while index_alphabets <= index_number:
                        index_number -= index_alphabets
                    if index_number == index_alphabets:
                        index_number = 0
                elif number < 0:
                    index_number = number
                    while index_number < (index_alphabets * (-1)):
                        index_number -= (index_alphabets * (-1))
                    if index_number == (index_alphabets * (-1)):
                        index_number = l
                    else:
                        index_number = index_number + l

                letter = alphabets[index_number]
                word_new = word_new+letter
    file_new = open("task04.txt", "wt", encoding='utf-8')
    file_new.write(word_new)
    print(word_new)


print("Введите слово :")
Shifr(str(input()))


def AntyShifr(file):

    print("Введите ключ шифрования :")
    number = int(input())

    index_alphabets = 26
    for index, line in enumerate(file):
        for i in range(0, len(line)):
            if index == i:
                word = str(line)[1:]
                for j in range(0, len(word)):
                    for l in range(0, len(alphabets)):
                        if word[j] == alphabets[l]:
                            index_number = 0
                          
                            if number > 0:
                                index_number = l - number
                                if abs(index_number) > index_alphabets:
                                    while abs(index_number) > index_alphabets:
                                        number = number - index_alphabets
                                        index_number = number
                                index_number = l - number
                           
                            elif number < 0:
                                index_number = number * (-1) + l
                                while index_alphabets <= index_number:
                                    index_number -= index_alphabets
                                if index_number == index_alphabets:
                                    index_number = 0

                            print(alphabets[index_number], end="")


with open("task04.txt", "r", encoding='utf-8') as file:
    AntyShifr(file)
