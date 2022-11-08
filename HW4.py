# 1. Вычислить число c заданной точностью d

#  Пример:
# при d = 0.001, π = 3.141.  10-1 ≤ d ≤10-10

# from math import pi

# d =  int(input("Ввести число: "))
# print(f'Пи с заданной точностью {d} равно {round(pi, d)}')

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Ввести число N: "))
# i = 2 
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа N {old} представлены в списке: {lst}")

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


# lst = list(map(int, input("Ввести числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список элементов: {new_lst}")


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.


# from random import randint

# def pol(k):
#     newPol = ''
#     for i in range(0, k+1):
#         digit = randint(1, 100)
#         if k == 0:
#             polynomial = (f'{digit} = 0')
#         elif k == 1:
#             polynomial = (f'{digit}x + ')
#         else:
#             polynomial = (f'{digit}x^{k} + ')
#         newPol += polynomial
#         k -= 1
#     return newPol

# k = int(input('Ввести натуральное число степени: '))
# result = pol(k)
# print(result)

# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# with open('poly_1.txt', 'w', encoding='utf-8') as file:
#     file.write('2*x^2 + 5*x^5')
# with open('poly_2.txt', 'w', encoding='utf-8') as file:
#     file.write('23*x^4 + 9*x^6')

# with open('poly_1.txt','r') as file:
#     poly_1 = file.readline()
#     list_of_poly_1 = poly_1.split()


# with open('poly_2.txt','r') as file:
#     poly_2 = file.readline()
#     list_of_poly_2 = poly_2.split()

# print(f'{list_of_poly_1} + {list_of_poly_2}')
# sum_poly = list_of_poly_1 + list_of_poly_2

# with open('sum_poly.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{list_of_poly_1} + {list_of_poly_2}')

