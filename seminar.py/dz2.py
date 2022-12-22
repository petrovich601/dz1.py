# Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


# x = (input('Введите вещественное число: '))
# my_list = len(x)
# m = float(x)
# t = 0
# if m < 0:
#     m = m * -1
# m = m * (10**my_list)   
# while m > 1:
#     t = int(t + (m % 10))
#     m = m // 10
# print(f"сумма цифр {t} ")


# Задайте список из n чисел последовательности (1 + 1/n)**n,
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n = int(input('Введите число N: '))
# rezalt = []
# sum = 0
# for i in range(n):
#     rezalt.append((1 + 1/(i+1))**(i+1))
#     rezalt[i] = round(rezalt[i], 2)
#     sum = sum + rezalt[i]
# print(f"Для N = {n}: ->", end=" ")
# print(rezalt, sep=", ")
# print(f"Сумма {sum}:")


# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ
# ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки
# Random для и получения случайного int


# n = int(input('Введите размер списка N: '))
# import random
# sps = []
# for i in range(n):
#     sps.append(random.randint(0,100))
# print("Исходный список: ", sps)
# for i in range(n):
#     j = random.randint(0, n-1)
#     element=sps.pop(j)
#     sps.append(element)
# print("Перемешанный список: ", sps)
