#     # Задача 1
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те
# числа, которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки.
var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел

a = set(var2.split()) 
b = set(var3.split()) 
s_set = sorted(a.intersection(b)) 
print(*s_set)

    # Вариант 2 авто тест не принял
var1 = input("Введите кол-во эл. 1 и 2 набора чисел через пробел: ")
var2 = input("Введите эл. 1 набора через пробел: ")
var3 = input("Введите элементы 2 набора через пробел: ")

n, m = map(int, var1.split())
first_set = set(map(int, var2.split()))
second_set = set(map(int, var3.split()))
common_elements = sorted(first_set.intersection(second_set)) # Находим общие элементы и выводим их в порядке возрастания
print("Числа встречаются в 1 и 2 наборах: ", *common_elements)

    # Вариант 3 авто тест не принял
n, m = [int(var1.split())]
first_set = set()
for num in var2.split():
    first_set.add(int(num))
second_set = set()
for num in var3.split():
    second_set.add(int(num))
common_elements = sorted(first_set.intersection(second_set))
print("Числа встречаются в 1 и 2 наборах:", *common_elements)



    # Задача 2
# В фермерском хоз-ве в Карелии выращивают чернику. Черника растет на
# круглой грядке, и кусты черники высажены по окружности грядки.
# Каждый куст черники имеет урожайность, которая соответствует кол-ву
# ягод на этом кусте. Урожайность черничных кустов представлена в виде
# списка arr, где arr[i] - это урожайность(количество ягод) i-го куста.
# В фермерском хоз-ве внедрена система автоматич сбора черники. Эта
# система состоит из управляющего модуля и нескольких собирающих
# Каждый собирающий модуль может собрать ягоды с одного куста и с двух
# соседних кустов. Собирающий модуль находится перед определенным
# кустом, и он может выбирать, с какого куста начать сбор ягод.
# Напиши программу, которая определит максимальное число ягод, которое
# может собрать один собирающий модуль за один заход, находясь перед
# некоторым кустом грядки.
# Вход: подается спис arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность
#  i-го куста черники. Размер списка не превышает 1000 элементов.
# Программа должна вывести одно целое число - макс кол-во ягод,
# которое может собрать собирающий модуль, находясь перед некоторым
# кустом грядки.

arr = [5, 8, 6, 4, 9, 2, 7, 3] 
 
max_summa = 0 
for i in range(len(arr)):  
     if max_summa < arr[i - 1] + arr[i] + arr[(i + 1) % len(arr)]: 
        max_summa = arr[i - 1] + arr[i] + arr[(i + 1) % len(arr)] 
print(max_summa)


