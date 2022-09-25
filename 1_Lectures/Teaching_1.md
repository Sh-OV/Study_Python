# Почему PYTHON?

Кроссплатформенность

Подходит для:
Веб-сервисов, ML, DataSciece, Аналитики, Игр, Написания софта
Интерпретируемый

##Основы основ

Как установить

https://www.python.org/downloads/

## Переменные

Типы данных справедливы

int, float, boolean, str,
list и др.

Python – язык с динамической типизацией

value = 2809

name = 'Sergey'

У Python есть одна проблема - 
Неверно поставленный пробел сломает вашу
программу

## Ввод и вывод данных

print() – отвечает за вывод данных

input() – отвечает за ввод данных

print('Введите а');

a = input()

print('Введите b');

b = input()

print(a, b)

print('{} -- {}'.fotmat(a, b))

или

print('Введите а');

a = int(input())

print('Введите b');

b = int(input())

c = 30

print(a, ' + ', b, ' = ', c)

print('{} + {} = {}'.format(a, b, c))

Пример:

print('Введите а');

a = input() # 10

print('Введите b');

b = input() # 20

c = 30

print(a, ' + ', b, ' = ', c) # 10 + 20 = 30

## Арифметические операции

Важно и нужно, без них вы не напишете ни одной
программы

Если помните математику – проблем не будет

+, -, * , /, %, //, **

Приоритет операций:

**
, ⊕, ⊖,
*
, /, //, %, +, -

( ) Скобки меняют приоритет

## Сокращённые операции и операции присваивания

iter = 2

iter += 3 # iter = iter + 3

iter -= 4 # iter = iter - 4

iter *= 5 # iter = iter * 5

iter /= 5 # iter = iter / 5

iter //= 5 # iter = iter // 5

iter %= 5 # iter = iter % 5

iter **= 5 # iter = iter ** 5

### Дополнительно

Демонстрация

a, b, c = 1, 2, 3   # a: 1 b: 2 c: 3

print('a: {} b: {} c: {}'.format(a, b, c))

range(*(1,5,2)))

## Логические операции
>, >=, <, <=, ==, !=

not, and, or – не путать с &, |, ^

Кое-что ещё: is, is not, in, not in

## Управляющие конструкции: if, if-else

Условный оператор позволяет управлять ходом
выполнения программы

if condition:

  operator 1

  operator 2

  ...

  operator n

else:

  operator n + 1

  operator n + 2

  ...

  operator n + m

  или

  if condition1:

   operator

elif condition2:

   operator

elif condition3:

   operator

else:

   operator 

## Управляющие конструкции: while

while condition:

   operator 1
   
   operator 2

   . . .

   operator n

## Управляющие конструкции: while-else

while condition:

   operator 1

   operator 2

   . . .

   operator n

else:

   operator n + 1

   operator n + 2

   . . .

   operator n + m

## Управляющие конструкции: for

Когда мы знаем что хотим )))

for i in enumeration:

   operator 1

   operator 2

   . . .

   operator n

#### *Знакомьтесь – range*

r = range(5) # range(0, 5)

r = range(2, 5) # range(2, 5)

r = range(-5, 0) # range(-5, 0)

r = range(1, 10, 2) # range(1, 10, 2)

r = range(100, 0, -20) # range(100, 0, -20)

Пример:

r = range(100, 0, -20) # range(100, 0, -20)

for i in r:

 print(i)

 получится: 100 80 60 40 20

for i in range(5):

 print(i)

получится: 0 1 2 3 4

## Немного о строках

text = 'съешь ещё этих мягких французских булок'

print(len(text)) # 39

print('ещё' in text) # True

print(text.isdigit()) # False

print(text.islower()) # True

print(text.replace('ещё','ЕЩЁ')) #

for c in text:

 print(c)


## Списки: введение

Список – пронумерованная, изменяемая коллекция
объектов НЕпроизвольных типов 

numbers = [1, 2, 3, 4, 5]

print(numbers) # [1, 2, 3, 4, 5]

numbers = list(range(1, 6))

print(numbers) # [1, 2, 3, 4, 5]

numbers[0] = 10

print(numbers) # [10, 2, 3, 4, 5]

for i in numbers:

 i *= 2

 print(i) # [20, 4, 6, 8, 10]

print(numbers) # [10, 2, 3, 4, 5]

Продолжение темы:

colors = ['red', 'green', 'blue']

for e in colors:

 print(e) # red green blue

for e in colors:

 print(e*2) # redred greengreen blueblue

colors.append('gray') # добавить в конец

print(colors == ['red', 'green', 'blue', 'gray']) # True

colors.remove('red') #del colors[0] # удалить элемент

## Функции

Это фрагмент программы, используемый
многократно

def function_name(x):

  body line 1

  . . .

  body line n

  optional return

Разбираемся дальше:

def f(x):

 return x**2
 
def f(x):

 if x == 1:

 return 'Целое'

 elif x == 2.3:

 return 23

 else:

 return

 print(f(1)) # Целое

print(f(2.3)) # 23

print(f(28)) # None

print(type(f(1))) # str

print(type(f(2.3))) # int

print(type(f(28))) # NoneType

