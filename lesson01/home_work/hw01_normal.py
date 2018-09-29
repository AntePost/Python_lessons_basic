
__author__ = 'Ваши Ф.И.О.'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# Normal, task 1, first version
# С циклом for и len()
num = 58375
num_str = str(num)
i = 0
j = 0
while i < len(num_str):
    for char in num_str:
        if j < int(char):
            j = int(char)
    i += 1
print("Number is %s" % num_str)
print("The biggest digit in this number is", j)

# Normal, task 1, second version
# Без цикла for и len()
num = 58375
print("Number is %d" % num)
j = 0
while num != 0:
    if j < num % 10:
        j = num % 10
    num = num // 10
print("The biggest digit in this number is", j)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

# Normal, task 2
# Через кортежи, а через арифметику решено в Easy-задании
var_a = input("Enter a variable: ")
var_b = input("Enter another variable: ")
var_a, var_b = var_b, var_a
print("First variable is now:", var_a)
print("Second variable is now:", var_b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# Normal, task 3
import math


coef_a = float(input("Enter coefficient a: "))
coef_b = float(input("Enter coefficient b: "))
coef_c = float(input("Enter coefficient c: "))
D = coef_b ** 2 - 4 * coef_a * coef_c
if D < 0:
    print("Discriminant is:", D)
    print("Your equation has complex roots. :(")
elif D == 0:
    x = -coef_b / (2 * coef_a)
    print("Discriminant is:", D)
    print("The only root is", x)
else:
    x_1 = (-coef_b - math.sqrt(D)) / (2 * coef_a)
    x_2 = (-coef_b + math.sqrt(D)) / (2 * coef_a)
    print("Discriminant is:", D)
    print("First root is:", x_1)
    print("Second root is:", x_2)
