  # Задача 1
# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1
list_1 = [int(i) for i in input("Введите числа: ").split()]
k = int(input("Введите число: "))
count = 0
for i in range(len(list_1)):
  if list_1[i] == k:
    count += 1
print(count)



  # Задача 2
# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному
# числу k и вывести его. Считать, что такой элемент может быть только один. Если
# значение k совпадает с этим элементом - выведите его

list_1 = [int(i) for i in input("Введите числа: ").split()]
k = int(input("Введите число: "))

near_value = list_1[0]
for el in list_1:
  if (k - el) ** 2 < (k - near_value) ** 2:
    near_value = el
print(f"Самый близкий элемент к {k} в массиве {list_1}: {near_value}")

    # Эталонное решение
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
  if m > abs(list_1[i] - k):
    m = abs(list_1[i] - k)
    number = list_1[i]
print(number)

  # Вриант 2
near_value = list_1[0] 
for el in list_1:
  if abs(el - k) < abs(near_value - k):
    fnear_value = el
print(near_value)

  # Вриант 3
m = min(list_1, key=lambda x: abs(x-k))
print(m)



  # Задача 3
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова
# k и выводит его. Будем считать, что на вход подается только одно слово, которое
# содержит либо только английские, либо только русские буквы.
k = input("Введите слово: ")
price = {1:'AEIOULNSTRАВЕИНОРСТ', 2:'DGДКЛМПУ', 3:'BCMPБГЁЬЯ', 4:'FHVWYЙЫ', 
         5:'KЖЗХЦЧ', 8:'JXШЭЮ', 10:'QZФЩЪ'}
total_value = 0
for i in k.upper():
  for key in price:
    if i in price[key]:
      total_value += key
print(total_value)

     # Эталонное решение
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
  if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    for j in points_en:
      if i in points_en[j]:
        count = count + j
  else:
    for j in points_ru:
      if i in points_ru[j]:
        count = count + j
print(count)

  # Решение Дениса (здсь алфовит ключ, а стоимость значение)
word = import("Введите слово: ")
data = {"A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т": 1,
        "D, G, Д, К, Л, М, П, У": 2,
        "B, C, M, P, Б, Г, Ё, Ь, Я": 3,
        "F, H, V, W, Y, Й, Ы": 4,
        "K, Ж, З, Х, Ц, Ч": 5,
        "J, X, Ш, Э, Ю": 8,
        "Q, Z, Ф, Щ, Ъ": 10}
# print(list(data.keys())) # тип данных dict_key чтобы стал списков указываем list
count = 0
for i in word: # Проходит по каждой букву в слове
  for key in data: # Проходит по каждому ключу внутри словоря
    if i.upper() in key: # Если в нутри ключа есть буква
      count += data[key] # То переменная увличивается на значение под данным ключем
print(count)