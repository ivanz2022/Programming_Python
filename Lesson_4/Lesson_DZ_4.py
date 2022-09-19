#1. Вычислить число c заданной точностью d
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
d = 5
print(round(math.pi, d))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
num = 124
lst = []
i = 2
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(lst)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

lst = [2, 2, 5, 3, 5, 6, 8, 7, 3, 8, 1, 1]
lst2 = []
i = 0
while i < len(lst):
    j = i + 1
    while j < len(lst):
        if lst[i] == lst[j]:
            lst2.append(lst[i])
        j += 1
    i += 1
final_lst = set(lst) - set(lst2)
print(list(final_lst))

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
def rnd():
    rnd = random.randint(0, 100)
    return rnd

k = 2
line = f'{rnd()}x*{k} + {rnd()}*x + {rnd()} = 0'
with open('file.txt', 'w') as file_wr:
    file_wr.write(line)