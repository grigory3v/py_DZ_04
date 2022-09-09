# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time
# или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)


import time

ns = time.time_ns() // 10** 6
sec = time.time() % (24 * 3600)
random = ns - sec
random = random % 10
random= round(random, 1)

random = random * 10
random = int(random)
print(random)
