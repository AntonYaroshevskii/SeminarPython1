#Задача 2: Найдите сумму цифр трехзначного числа.
# a = int(input('Введите трехзначное число: '))
# print(f'Сумма числа {a} равна = {(a % 10) + (a % 100 // 10) + (a // 100)}')

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# b = int(input('Введите количество сделанных журавликов: '))
# P = (b // 3) // 2
# S = (b // 3) // 2
# K = b - P - S
# if (K // 2 != P + S):
#     print('количество журавликов не подходит под условие задачи')
# else:
#     print(f'Петя сделал {P} журавликов,Сережа сделал {S} журавликов, Катя сделала {K} журавликов')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют
# такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# n = int(input('Введите номер вашего билетика: '))
# a = n // 1000
# b = n % 1000
# sum1 = (a % 10) + (a % 100 // 10) + (a // 100)
# sum2 = (b % 10) + (b % 100 // 10) + (b // 100)
# if (sum1 == sum2):
#     print('Счастливый билетик')
# else:
#     print('Не счастливый билетик')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между
# дольками (то есть разломить шоколадку на два прямоугольника).

# n = int(input('Введите число строк шоколадки: '))
# m = int(input('Введите число столбцов шоколадки: '))
# k = int(input('Введите количество долек которые хотим отломить от шоколадки: '))
# if n * m > k:
#     if (k % n == 0) or (k % m == 0):
#         print('yes')
#     else:
#         print('no')
# else:
#     print('невыполнимое условие')
