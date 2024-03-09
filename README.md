# Python-1
Знакомство с языком Python

### Визуализатор
## [Показывает код и его поэтапную работу](https://pythontutor.com/)


### __print(sep=' ')__ 
*- sep='пробел' разделитель между переменными в принте по умолчанию. Для того, что бы разжелителем являлось что то другое, необходимо праписать следующим образом* 

print(a, b, z, sep='необходимый знак')


### __print(end='\n\')__ 
*- end='\n' перенос на новую строку после выведения принта, так же можем в место '\n', прописать '\t'(табуляуию) или ' '(пробел).*


### __print(*s, '\n')__ 
_- (*s) при выводе на экран, какждый элементсимвол списка, строки, массива выводит отдельным элементом. А '\n' выведет каждыйэлемент с новой строки._

### Форматирование
name = 'John'

age = 25

print('Привет, меня зовут {}, мне {} лет.'.format(name, age))

print('Привет, меня зовут {a}, мне {b} лет.'.format(a = name, b = age)) (2й вариант)

### Функчия __range__ (диапазон чисел)
*range(start=0, stop, step=1)

range(5) -> range(start=0, stop=5, step=1) ->0,1,2,3,4

range(2, 10) -> range(start=2, stop=10, step=1) ->2,3,4,5,6,7,8,9

range(3, 15, 2) -> range(start=3, stop=15, step=2) ->3,5,7,9,11,13*

### Оператор __continue__ и __break__
for num in range(50):

  if num % == 0:

    continue (Прерывает операшию и цикл начинается со след num)
  if num % 3 == 0:

    print(num, end=' ')
  if num == 33:

    break (Завершает весь цикл и в else нен попадаем)

else:

  print('Я все, закончил!')
  