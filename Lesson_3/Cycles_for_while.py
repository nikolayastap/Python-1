#   # Задача 9
# # По данному целому неотрицательному n вычислите значение n!. N! = 1*2*3*...*N
# # (произведение всех чисел от 1 до N, Факториал) 0! = 1 
# # Рещите задачу используя уикл while

# n = int(input(Введите число))
# count = 1
# factorial = 1

# while count <= n:
#   factorial *= count
#   count += 1

# print(factorial)

        # 2 вариант
# n = int(input(Введите число))
# factorial = 1

# while n < 1:
#   factorial *= n
#   n -= 1

# print(factorial)



#   # Задача 11
# # Дано натуральное число А > 1. Определите, каким по счету числом Фибоначчи оно
# # является, то есть выведитте такое число n, что ф(n) = А. Если А не является
# # числом Фибоначчи, выведите число -1
# #  0 1 1 2 3 5 8 13

# n = int(input("Ввеите число Фибоначчи: "))
# fib_0 = 0
# fib_1 = 0
# fib_2 = 1
# count = 2

# while fib_0 < n:
#   fib_0 = fib_1 + fib_2
#   fib_1 = fib_2
#   fib_2 = fib_0
#   count +=1
#   if fib_0 > n: # Есл не является числом Фибоначи
#     count = -1
# print(count) # Выводим порядковый номер или -1

#         # 2 вариант
# n = int(input("Ввеите число Фибоначчи: "))
# fib_0 = 1
# fib_1 = 2
# count = 4

# while fib_1 < n:
#   fib_0, fib_1 = fib_1, fib_0 + fib_1
#   count +=1

# if fib_1 != n:
#     print("-1")
# else:
#     print(count)



#   # Задача 13
# # Уставшие от теплой зимы, жители решили узнать, действительно ли это самая длин
# # оттепель за всюисторию наблюдений за погодой. Они обратились к синоптикам, а 
# # те, в свою очаредь, занялись исследованиями статистики за прошлые годы. Их
# # интересует, сколько дей длилась самая длинная оттепель. Когда среднесуточная
# # температура ежедневно превышала 0 градусов Цельсия. Напишите программу 
# # помогающая синоптикам в работе.
# # Пользователь вводит число N - общ. кол-во расматриваемых дней (1 <= N <= 100).
# # В следующих строках распологается N целых чисел.
# # Каждое число - среднесуточная темер. в соответствующий день. Температуры - целые
# # числа и лежат в диапазоне от -50 до 50

# n = int(input())
# k = 0 # Кол-во дней сколько длится оттепель
# max = 0 # Кол-во самой длинной оттепели за все расматриваемое время
# for i in range(n):
#   x = int(input()) # x - вводим температуру
#   if x > 0: # Если темп. > 0
#     k += 1
#   else:
#     if max < k: # Если мах оттепель больше чем текущая
#       max = k
#     k = 0

# print(max)

#         # 2 вариант
# from random import randint # Функция будет использоватьсядля рандомного вывода температуры

# days = int(input('Введите кол-во дней: '))
# count = 0
# max_count = 0

# for _ in range(days):
#   temp = randint(-50, 50) # Получение температуры в каждый день рандомно
#   print(temp, end=' ')
#   if temp > 0:
#     count += 1
#     if count > max_count:
#       max_count = count
#   else:
#     count = 0

# print()
# print(max_count)

#         # 3 вариант
# from random import randint # Функция будет использоватьсядля рандомного вывода температуры

# days = int(input('Введите кол-во дней: '))
# count = 0
# max_count = 0

# for _ in range(days):
#   temp = randint(-50, 50) # Получение температуры в каждый день рандомно
#   print(temp, end=' ')
#   if temp > 0:
#     count += 1
#   else:
#     if count > max_count:
#       max_count = count
#     count = 0
# if count > max_count:
#   max_count = count

# print()
# print(max_count)



#   # Задача 15
# # Иван Вас пришел на рынок и решил купить 2 арбуза: 1 для себя, другой для тещи.
# # Для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот не задача:
# # арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый.
# # Пользователь вводтит одно число N -кол-во арбузов. Вторая строка содержит N
# # чисел, записанных на новой строчке каждое. Здесь каждое число - это масса
# # соответствуещего арбуза. Все числа натуральные и не привышают 3000

# n = int(input()) # Кол-во арбузов
# max = -1 # Минимально возможный вес 
# min = 3001 # Максимально возможный вес 

# for i in range(n):
#   x = int(input()) # Вводим вес 
#   if x > max:
#     max = x
#   if x < min:
#     min = x

# print(min, max)

#         # 2 вариант
# from random import randint

# n = int(input('Введите кол-во арбузов: '))
# min_weight = float('inf') # Максимально допустимое число
# max_weight = -float('inf') # Минимально допустимое число

# for _ in range(n):
#   weight = randint(1, 3001)
#   print(weight, end=' ')
#   min_weight = min(weight, min_weight)
#   max_weight = max(weight, max_weight)

# print()
# print(f'{max_weight = } кг, {min_weight = } кг')