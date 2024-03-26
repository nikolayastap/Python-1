    # Задача 1
# Напишите функц print_operation_table(operation, num_rows, num_columns),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по
# номеру строки и столбца. По умолчанию номер столбца и строки = 9.
# Аргументы num_rows и num_columns указывают число строк и столбцов
# таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст:
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

# Эталонное решение
def print_operation_table(operation, num_rows=9, num_columns=9):
  result = []
  if num_rows < 2 or num_columns < 2:
    print('ОШИБКА! Размерности таблицы должны быть больше 2!')
  else:
    for i in range(1, num_rows + 1):
      for j in range(1, num_columns + 1):
        if j != num_columns :
          result.append(f'{operation(i, j)} ')
        else:
          result.append(operation(i, j))
      result.append('\n')
    print(''.join([str(i) for i in result[:len(result) - 1]]))


def print_operation_table(operation, num_rows=9, num_columns=9):
  # Проверка на правильность размерности таблицы
  if num_rows < 2 or num_columns < 2:
    print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    return
  # Вывод строк таблицы с результатами операции
  for i in range(1, num_rows + 1):
    row_result = [operation(i, j) for j in range(1, num_columns + 1)]
    print(*row_result)

# Примеры использования функции с различными операциями и размерностями таблицы
print_operation_table(lambda x, y: x * y, 3, 3)
# print_operation_table(lambda x, y: x + y, 4, 4)
# print_operation_table(lambda x, y: x - y, 5, 5)
# print_operation_table(lambda x, y: x * y, 1, 2)
# print_operation_table(lambda x, y: x / y, 4, 4)
# print_operation_table(lambda x, y: x * y)



    # Задача 1
# Винни-Пух попросил посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он
# их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных
# букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух передаст вам автоматически в переменную
# stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом
# все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо
# вывести: Количество фраз должно быть больше одной!.

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
def count_vowels(word):
    vowels = "аеёиоуыэюя"
    return sum(1 for letter in word if letter.lower() in vowels)

def check_rhythm(poem):
    phrases = poem.split()
    if len(phrases) <= 1:
        print("Количество фраз должно быть больше одной!")
        return

    syllables_count = None
    for phrase in phrases:
        words = phrase.split("-")
        phrase_syllables = sum(count_vowels(word) for word in words)
        if syllables_count is None:
            syllables_count = phrase_syllables
        elif phrase_syllables != syllables_count:
            print("Пам парам")
            return
    print("Парам пам-пам")

check_rhythm(stroka)

# Эталонное решение
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka.split()
if len(phrases) < 2:
 print('Количество фраз должно быть больше одной!')
else:
 countVowels = []
 for i in phrases:
  countVowels.append(len([x for x in i if x.lower() in vowels]))
 if countVowels.count(countVowels[0]) == len(countVowels):
  print('Парам пам-пам')
 else:
  print('Пам парам')