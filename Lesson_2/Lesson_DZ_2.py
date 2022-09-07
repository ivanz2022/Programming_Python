from random import randint

# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0.56 -> 11

num = "0.56"
total = 0
for i in num:
    if i != '.':
        total += int(i)
print(total)

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = 4
total = 1
for i in range(1, num+1):
    total *= i
    print(total)

# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

num = 4
lst = []
for i in range(num):
    seq = (1+1/num)**num + i
    lst.append(seq)
print(lst)   
total = 0
for j in lst:
    total += j
print(f'Сумма последовательности равна: {total}')

# 4.(ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

num = 5
file_wr = open('file.txt', 'w')
for i in range(num):
    rnd = randint(-num, num)
    file_wr.write(str(rnd) + '\n')
file_wr.close()

file_rd = open('file.txt', 'rt')
total = 1
for i in file_rd:
	total *= int(i)
file_rd.close()

print(f'Произведение элементов в файле равно: {total}')

# 5. Реализуйте алгоритм перемешивания списка

lst = [3, 6, 'text', 7.5, 'textt']
print(lst, end=' ' + '\n')

i = 0
while i < len(lst):
    rnd = randint(1, 4)
    temp = lst[i]
    lst[i] = lst[rnd]
    lst[rnd] = temp
    i += 1
print(lst, end=' ')