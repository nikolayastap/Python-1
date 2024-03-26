    # Функции высшего порядка

# lambda() - упрощает функцию
# map() - примеяет функцию которой передаем 1м параметром к каждому эл переданной колекции данных
a, b = map(int, input().split()) # создает список(input) строк через пробел(split) и map применяет к каж эл функцию int
print(a + b)


    # Задача №47
# Есть код, который не можете менять (часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак
# преобразовывать список значений, а нужно получить его как есть.
# Напишите лямбда-выражение transformation, чтобы transformed_values
# получился копией values

# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# ->> ok


trasformation = lambda x: x # берем список применяем функцию в которой передаем x (приняли х и возратили х)
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(trasformation, values)) # map итерирует каждое значение передоваемого списка и применяет функцию values
if values == transformed_values:
  print('ok')
else:
  print('fail')



    # Задача №49
# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой
# далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди
# списка орбит планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды
# таких планет нет, зато искусственные спутники были запущены на
# круговые орбиты. Результатом функции должен быть кортеж, содержащий
# длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины
# полуосей эллипса. При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить
# самую большую площадь эллипса, а затем найти и сам эллипс, имеющий
# такую площадь. Гарантируется, что самая далекая планета ровно одна

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# ->> 2.5 10

from math import pi # Импортируем из библиотеки число ПИ

def find_farthest_orbit(list_of_orbits):
  list1 = [i for i in list_of_orbits if i[0] != i[1]] # Записываем значения где 1е число картежа не равно 2му
  list_s = [(pi * i[0] * i[1]) for i in list1] # Список в котором считаем площади каждого элепса
  max_s = list_s.index(max(list_s)) # Возращаем индекс из списка площадей. index() - находит значение и возращает индекс

  return list1[max_s] # возврощаем эл с индексом max_s

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))


# Обяснение Дениса (Нет смысла сравнивать числа умноженные на pi, тк это в итоге не поменяет резуьтат при сравнеии)
def find_farthest_orbit(orbits):
  list_square = [(i[0] != i[1]) * i[0] * i[1] for i in orbits] # Проверяем на неравность эл картежа, после проверки умнажаем эл в каждом картеже между собой
  # return list_square # 3 25 14 0 12 - 0 тк сравнение дало False а он в типе дпнных int = 0
  return orbits[list_square.index(max(list_square))] # index в нутри заданого списка list_square ищет индекс, где находится максимал значение даноого списка(max(list_square))

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits)) # (2.5, 10) - вывели эл в списке orbits 

    # Задача №51
# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и
# возвращают True, если это так. Если значение характеристики для разных
# объектов отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это функция, которая
# принимает объект и вычисляет его характеристику.

# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
#   print('same')
# else:
#   print('different')
# ->> same

def same_by (characteristic, objects):
  result = True # Создали переменную в которой храним результат функции
  list1 = [characteristic(x) for x in objects] # Результат работы функции к спису
  for i in range(len(list1) -1): # Сравниваем все эл, за исключением поседнего эл тк возьмет его при проверке условия
    if list1[i] != list1[i + 1]:
      result = False
  return result

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
  print('same')
else:
  print('different')

# Решение одного из сокурсников
def same_by(f, num):
  list_c = list(map(f, num))
  for i in list_c:
    if list_c[0] != i:
      return False
  return True
value = [2, 4, 0, 8]
if same_by(lambda x: x % 2, value):
  print('same')
else:
  print('different')


# Обяснение Дениса 54.30
def same_by(characteristic, objects):
  return len(set(list(map(characteristic, objects)))) in (0, 1) # list - в список, set - в можество
        # множ не может в себе хранить одинаковык эл, если все знач = то множество = 1 возтащаем True
        # если ни чего не пережается то = 0

values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
  print('same')
else:
  print('different')