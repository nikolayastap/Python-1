#   # Опреднлеие типа данных
# n = "rtyu"
# print(type(n))



#   # Интерполяция
# a = 5
# b = 5.89
# c = 'Hello'

# print(a,b,c)
# print(a, '-', b, '-', c) # Через дефис
# print(f"{a} - {b} - {c}") # f строки
# print("{} - {} - {}".format(a,b,c)) # .format



#   # Ввод данных с помощю функции input
# print('Введите первую число: ') # Приглашение к вводу
# a = input() # Запрос ввода с клавиатуры с промощю input, и далльнейшее присвоение к переменной a
# b = input('Введите второе число: ') # 2й способ
# print(a, '+', b, ' = ', a + b) # Вывод сумирует строки, а не значеие



#   # Приведение типов(для коректного действия)
# c = 5.89
# print(c)
# print(type(c))
# c = int(c) # Переменную float переводим в int
# print(c)
# print(type(c))
# c = str(c) # Переменную int переводим в string
# print(c)
# print(type(c))
# c = bool(c) # Переменную string переводим в bool
# print(c)
# print(type(c))



#   # Ввод данных с помощю функции input (исправили)
# print('Введите первую число: ')
# a = int(input())
# b = int(input('Введите второе число: '))
# print(a, '+', b, ' = ', a + b) # Вывод сумирует строки, а не значеие



#   # Округление чисел
# a = 5.89956
# b = 6.556551
# print(round(a*b, 3))



#   # Сокращенное присвоение
# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 6 # iter = iter / 6
# iter //= 7 # iter = iter // 7
# iter %= 8 # iter = iter % 8
# iter **= 9 # iter = iter ** 8



#   # Логические операции
# a = 1 > 4
# print(a) # False
# a = 1 < 4 and 5 > 2
# print(a) # True
# a = 1 == 2
# print(a) # False
# a = 1 != 2
# print(a) # True
# a = 'qwe'
# b = 'qwe'
# print(a == b) # True
# a = 1 < 3 < 5 < 10
# print(a) # True



#   # Управляющие конструкции if, if-else
# username = input('Введите имя: ')
# if username == 'Маша':
#   print('Ура, это Маша!')
# elif username == 'Марина':
#   print('Я так ждала Вас, Марина')
# elif username == 'Ильнар':
#   print('Ильнар - топ')
# else:
#   print('Привет, ', username)



#   # Управляющая конструкция while-else
# i = 0
# while i < 5:
#   if i == 3:
#     break # использование не желательно
#   i = i + 1
# else:
#   print('Пожалуй')
#   print('хватит )')
# print(i)



#   # Метод флажка 
# # Программа находит мин делитель данного числа
# n = int(input())
# flag = True
# i = 2
# while flag:
#   if n % i == 0: # Если остаток при делеии числа n на i равен 0
#     flag = False
#     print(i)
#   elif i > n // 2: # Делить числа не может привышать введенное число, деленное на 2
#     print(n)
#     flag = False
#   i +=1



#   # Цикл for
# a = 'qwerty'

# for i in a: # переменная i по очередно(согласно индексу) принемает и выводит значение
#   print(i)


#     # Исползование вложеных циклрв
#   line = "" 
#   for i in range(5): #range генерирует последовательность из 5и чисел, тоесь цикл выполняется 5 раз
#     line = ""
#     for j in range(5):
#       line += "+"
#     print(line)



#   # Строки
# text = 'съЕШЬ ещё этих МяГкИх французских булочек'
# print(len(text)) # Фцнкция len позволяет узнать размер строки(любой колекции данных)
# print('ещё' in text) # Проверяет наличее в тексте, результат(True/False)
# print(text.lower()) # Функция lower позволяет веревести все буквы в нжний регистр
# print(text.upper()) # Функция upper позволяет веревести все буквы в верхний регистр
# print(text.replace('ещё', 'ЕЩЁ')) # Функция replace позволяет заменить (1м указываем какое, 2м на какое)



#   # Срезы (для более удобной работы со стороками)
# text = 'съешь ещё этих мягких французских булочек'
# print(text[0]) # Выводит элемент под индексом 0
# print(text[1]) # Выводит элемент под индексом 1
# print(text[len(text)-1]) # Чтобы вывести последний элемент
# print(text[-5]) # Чтобы вывести 5 элемент с конца
# print(text[:]) # Выводит весь текст
# print(text[:2]) # Выводит с [0] по [2]не включая его
# print(text[len(text)-2:]) # Выводит с предпослед эл до конца
# print(text[2:9]) # Начиная с второго до девчятого
# print(text[6:-18]) # С 6 до -18 
# print(text[0:len(text):6]) # От 0 до конца строки с шагом 6 (выводится кажый 6 эл)
# print(text[::6]) # От 0 до конца строки с шагом 6 (выводится кажый 6 эл)

# text = text[2:9] + text[-5] + text[:2] # берем с 2 по 9 + -5, с 0 по 2
# print(text)