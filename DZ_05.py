# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

def rle_encode(file): 
    encoding = '' 
    prev_char = '' 
    count = 1 
    if not file: return '' 
    
    for index, line in enumerate(file):
        for i in range(0, len(line)):
            data = str(line)


            for char in data:
                if char != prev_char:  
                    if prev_char: 
                        encoding += str(count) + prev_char 
                    count = 1 
                    prev_char = char 
                else: 
                    count += 1 
            else:  
                encoding += str(count) + prev_char 
                return encoding


with open("task05.txt", "r", encoding='utf-8') as file:
    encoded_val = rle_encode(file) 
print(encoded_val)


def rle_decode(data): 
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit():
            count += char 
        else: 
            decode += char * int(count) 
            count = '' 
    return decode

decoded_val = rle_decode(encoded_val) 
print(decoded_val)