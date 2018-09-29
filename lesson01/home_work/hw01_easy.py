
__author__ = 'Иван Кузнецов'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...

# Easy, task 1, first version
# Через цикл for
num = 58375
num_str = str(num)
print("Digits in number %s are:" % num_str)
for char in num_str:
    print(char)

# Easy, task 1, second version
# Через цикл while
num = 58375
num_str = str(num)
print("Digits in number %s are:" % num_str)
i = 0
while i < len(num_str):
    print(num_str[i])
    i += 1

# Easy, task 1, third version
# Через цикл while и арифметические операции
num = 58375
num_str = str(num)
print("Digits in number %s are:" % num_str)
i = 1
while i <= len(num_str):
    print(num % 10)
    num = num // 10
    i += 1

# Easy, task 1, fourth version
# Через цикл while и арифметические операции без использования len()
num = 58375
print("Digits in number %d are:" % num)
while num != 0:
    print(num % 10)
    num = num // 10

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# Easy, task 2, first version
# Через третью переменную
var_a = input("Enter a variable: ")
var_b = input("Enter another variable: ")
var_c = var_a
var_a = var_b
var_b = var_c
print("First variable is now:", var_a)
print("Second variable is now:", var_b)

# Easy, task 2, second version
# Через арифметические операции
var_a = float(input("Enter a number: "))
var_b = float(input("Enter another number: "))
var_a = var_a + var_b
var_b = var_a - var_b
var_a = var_a - var_b
print("First number is now:", var_a)
print("Second number is now:", var_b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# Easy, task 3
age = int(input("Введите Ваш возраст: "))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")
