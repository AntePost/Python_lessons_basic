# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

# Easy, task 1
orig_list = [1, 2, 4, 0]
sqr_list = [item ** 2 for item in orig_list]
print(sqr_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# Easy, task 2
fr_list_1 = ["apple", "banana", "grapefruit", "mango", "melon", "orange",
             "watermelon"]
fr_list_2 = ["apple", "mango", "watermelon"]

fr_list_3 = [item for item in fr_list_1 if item in fr_list_2]
print(fr_list_3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

# Easy, task 3
import random


num_list = [random.randint(-10, 40) for _ in range(20)]
num_list_2 = [item for item in num_list if (item > 0) and (item % 3 == 0) and
              (item % 4 != 0)]
print(num_list)
print(num_list_2)
