# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

# Easy, task 1
var_list = ["яблоко", "банан", "киви", "арбуз"]
i = 0
while i < len(var_list):
    print("{0}. {1:>10}".format(i+1, var_list[i]))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# Easy, task 2, version 1
# Через цикл while, использование второго while вместо if и remove нагуглил
# Почему-то не работает с pop, пишет, что out of range. Видимо потому, что pop
# требует индекса, а как с индексом эту задачу решить не догадался
var_list_1 = [1, 1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9]
var_list_2 = [1, 3, 5, 7, 9]
i = 0
while i < len(var_list_2):
    while var_list_2[i] in var_list_1:
        var_list_1.remove(var_list_2[i])
    i += 1
print(var_list_1)

# Easy, task 2, version 2
# Через цикл for, конструкцию с while и remove нагуглил
var_list_1 = [1, 1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9]
var_list_2 = [1, 3, 5, 7, 9]
for item in var_list_2:
    while item in var_list_1:
        var_list_1.remove(item)
print(var_list_1)

# Easy, task 2, version 3
# Через .pop(). Нерабочий вариант видимо из-за смещения индекса при удалении
var_list_1 = [1, 1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9]
var_list_2 = [1, 3, 5, 7, 9]
i = 0
for item in var_list_1:
    if item in var_list_2:
        var_list_1.pop(i)    
    i += 1
print(var_list_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# Easy, task 3
var_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
var_list_2 = []
for item in var_list_1:
    if item % 2 == 0:
        var_list_2.append(item / 4)
    elif item % 2 != 0:
        var_list_2.append(item * 2)
print(var_list_2)
