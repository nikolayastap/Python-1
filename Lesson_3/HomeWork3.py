#   # Задача 1
# # На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые
# # – гербом. Ваша задача - определить минимальное количество монеток, которые нужно
# # перевернуть, чтобы все монетки лежали одной и той же стороной вверх.
# # На вход программе подается список coins, где coins[i] равно 0, если i-я монетка
# # лежит гербом вверх, и равно 1, если i-я монетка лежит решкой вверх. Размер
# # списка не превышает 1000 элементов.
# # Программа должна вывести одно целое число - минимальное количество монеток,
# # которые нужно перевернуть.

# coins = [0, 1, 0, 1, 0]
# eagle = 0
# tails = 0
# min = 0

# for coins in coins:
#   if coins == 1:
#     eagle += 1
#   else:
#     tails += 1
# if eagle > tails:
#   min = tails
# else:
#   min = eagle

# print(min)



#   # Задача 2
# # Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает
# # Кате по математике.Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя
# # должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих
# # чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# # Примечание: числа S и P задавать не нужно, они будут передаваться в тестах. В
# # результате вы должны вывести все возможные пары чисел X и Y через пробел, такие
# # что X <= Y.

# s = 12
# p = 27

# x = 1
# y = 1

# for x in range(s):
#   for y in range(s):
#     if x * y == p and x + y == s and x <= y:
#       print(x, y)

#     # Вариант 2
# res = 0

# for x in range(1, s):
#   y = s - x
#   if x * y == p and x <= y:
#     res = (x, y)

# print(*res)



#   # Задача 3
# # Требуется вывести все целые степени двойки (т.е. числа вида 2k), не
# # превосходящие числа N.

# n = 16
# k = 1
# power_two = 1

# for k in range(n):
#   power_two = 2 ** k
#   if power_two <= n:
#     print(power_two)

#   # Вариант 2
# n = 16
# k = 0
# while 2 ** k <= n:
#     print(2 ** k)
#     k += 1