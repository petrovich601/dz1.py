
# 1. Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на позиции с нечетным
# индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# n = int(input('Введите размер списка N: '))
# import random
# sps = []
# for i in range(n):
#     sps.append(random.randint(0,100))
# print("Исходный список: ", sps)
# sum = 0
# nechet =[]
# for j in range(n):
#     if j % 2 != 0:
#         sum += sps[j]
#         nechet.append(sps[j])
# print(f"Нечетные элементы:", end=' ')
# print(*nechet, sep=', ')        
# print(f"Сумма нечетных элементов: {sum}")


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# my_list = []
# while True:
#     namber = input(f'Введите число: ')
#     if namber == '':
#         break
#     my_list.append(int(namber))
# sum = []
# n = len(my_list)
# if (n // 2) * 2 == n:
#     for i in range((n // 2)):
#         sum.append(my_list[i] * my_list[(n - 1 - i)])
# else:
#     for i in range((n // 2)+1):
#         sum.append(my_list[i] * my_list[(n - 1 - i)])
# print(sum)

# 3. Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной
# части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# my_list = []
# while True:
#     namber = input(f'Введите вещественное число: ')
#     if namber == '':
#         break
#     my_list.append(float(namber))
# print(my_list)
# dh = []
# for i in range(len(my_list)):
#     dh.append(round((my_list[i]) - int(my_list[i]), 5))
# max = 0
# min = 1
# for j in range(len(my_list)):
#     if dh[j] != 0:
#         if max < dh[j]:
#             max = dh[j]
#         if min > dh[j]:
#             min = dh[j]
# print(f'Искомая разница: {max-min}')


# 4. Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# n = int(input('Введите число: '))
# dv = []
# while n != 0:
#     dv.append(n % 2)
#     n = n // 2
# print(*dv)


# 5. Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

# n = int(input('Введите число: '))
# if n == 0:
#     print(0)
# else:
#     nf = [1, 0]
#     for i in range(1, n+1):
#         nf.insert(i+1, ((nf[i]) + (nf[i-1])))
#     nf.remove(nf[0])
#     nfn =[0, 1]
#     for j in range(1, n):
#         nfn.insert(j+1, ((nfn[j-1]) - (nfn[j])))
#     nfn.remove(nf[0])
#     for k in range(n):
#         element = nfn.pop(n - 1 - k)
#         nfn.append(element)
#     for m in range(n+1):
#         nfn.append(nf[m])
#     print(nfn)