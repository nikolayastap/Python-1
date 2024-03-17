# dict(dictionary) - словарь
# key: valye - ключ, значение
data = {"Ivan": 27, "Petr": 31, "Alina": 18, "Egor": 23,
        "Anna": 45, "Vladimir": 60, "Mariy": 19}
print(data.keys()) # Возвращаются все ключи
print(data.values()) # Возращаются все значения
print(data.items()) # Возвращается коллекция данных, которая содержит кортеж
        # Кортеж состоит из двух зачений (ключ, значение)

for i in data.keys: # Либо for i in data:
  print(i) # Выведет все ключи в столбик

for i in data.values(): # Либо for i in data:
  print(i)                      # print(data(i)) - Выведет все значения

data["Ivan"] = 35 # Добавит новую запись, если ключ Ivan есть то перезапишет значение
print(data)

data = {"Ivan": 27, "Petr": 31, "Alina": 18, "Egor": 23,
        "Anna": 45, "Vladimir": 60, "Mariy": 19, "Ivan": 20} # При таком добавлении "Ivan": 20 ошибки не будет
print(data) # Но при выводе будет показавать ключ "Ivan" с последним значением

  # Задача 25
# Программа принемает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Кол-во повторов добавл к символам с пом постфикса формата _n
# a a a b c a a d c d d -> a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

data = input("Введите символы через пробел: ").split()
print(data)
frequency_dict = {} # Чистотный словарь (считает сразу все повт сим)
for element in data:
  if element not in frequency_dict: # Если эл. не является ключем frequency_dict
    print(element, end=' ') # Тогда мы выводим его на экран, т.к. он встретился первый раз
    frequency_dict[element] = 1 # Заыодим запись, где ключем будет элемент,а значением будет 1
  else: # Иначе элемент является ключем данного словаря
    print(f'{element}_{frequency_dict[element]}', end=' ')
    frequency_dict[element] +=1

  # Вариант 2
stroka = input("Введите символы через пробел: ")
stroka = stroka.split() # Преобразовываем строку в массив
res = {}

for i in stroka:
  if i in res:
    print(f'{i}_{res[i]}', end=' ')
  else:
    print(i, end=' ')
  res[i] = res.get(i, 0) + 1


            # String(str)
name = "Petr"
print(name[0]) # Итерируемый обьект - можно обратиться по индексу
print(name[0:2]) # Можно делать срезы
print("Petr" < "petr") # т.к. станение проходит по таблице UTF-8
print(name.lower()) # Переводит буквы в нижний регистр
print(name.upper()) # Переводит буквы в верхний регистр
print(ord("A")) # Принемает символ таблици кодировки UTF-8 и возращает номе
print(chr(45)) # Принемает номер таблици кодировки UTF-8 и возращает символ
print([chr(i) for i in range(ord("A"), ord("Z") + 1)]) # Выведет алфовит по порядку в верхнем регистре



  # Задача 27
# Пользователь вводит текст(строка). Словом считается последовательность
# непробельных символов идущих подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов содержится в этом тексте.
# She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells 
# -> 13

text = input("Input text: ").lower()
separator = "!.,@:;№" # Разделитель
for i in separator:
  text = ''.join(text.split(i)) # split создаст массив без i(разделители), join - обьединяет все символы через пустую строчку
print(len(set(text.split()))) # set - переводим в множество, len - у множества ищем кол-во

  # Вартант 2 Решение в одну строку, при условии если из разделителей только пробелы
print(len(set(input("Input text: ").lower().split())))

  # Вариант 3
stroka = input("Input text: ").split() # Вводим даные и функц split() преобразовываем в массив
set_1 = set() # Создали пустое множество
for i in stroka:
  set_1.add(i.lower()) # add добавляет эл i в можество, преобразовав в маленьки регистр lower
print(len(set_1)) # len считает размер множеста



#   Задача 29
# Ваня и Петя поспорили,кто быстрее решит задачу: "Задана последоват. неотрицательных
# цулых чисел. Требуется определить значение наибольшего эл последовательности, которая
# завершается первым встретившимся нулем (число 0 не входит в последовательность)".
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца
# сделать задание.Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# Провеьте код
# Ваня -> 2                                 Петя -> 4
# n = int(input())                        n = int(input())
# max_number = 1000                       max_number = -1
# while n != 0:                           while n < 0:
#   n = int(input())                        n = int(input())
#   if max_number > n:                      if max_number < n:
#     max_number = n                          n = max_number
# print(max_number)                       print(n)

# n = int(input())                        n = int(input())
# max_number = n                          max_number = n
# while n != 0:                           while n > 0:
#   n = int(input())                        n = int(input())
#   if max_number < n:                      if max_number < n:
#     max_number = n                          max_number = n
# print(max_number)                       print(max_number)

