    # Задача 1
# Напишите функцию f, которая на вход принимает два числа a и b, и
# возводит число a в целую степень b с помощью рекурсии.
# a = 3; b = 5 -> 243  (3^5)
# a = 2; b = 3 -> 8

def f(a, b):
  if b == 0:
    return 1
  return a ** b
print(f(3, 5))

  # Эталонное решение
def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a
print(f(3, 5))



    # Задача 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются
# только +1 и -1. Также нельзя использовать циклы.
# sum(2, 2) -> 4

def sum(a, b):
  if a == 0:
    return b
  elif b == 0:
    return a
  else:
    return sum((a + 1), (b - 1))
a = 3
b = 5
print(sum(a, b))