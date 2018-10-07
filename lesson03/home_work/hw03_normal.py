# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# Normal, task 1
# Алгоритм подсмотрел на чужом форке, сделал по аналогии
def fibonacci(n, m):
    """
    Returns Fibonacci sequence from n to m
    """
    fib_list = [1, 1, 2]
    f1 = 1
    f2 = 1
    f_new = 2
    i = 3
    while i < m:
        f2 = f1
        f1 = f_new
        f_new = f1 + f2
        fib_list.append(f_new)
        i += 1
    return fib_list[n-1:]


print(fibonacci(9, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

# Normal, task 2
# Подсмотрел алгоритм в интернете и на чужом форке, списал оттуда, так что как
# правильное решение учитывать при оценке не надо. В коде разобрался
def sort_to_max(origin_list):
    """
    Sorts origin_list in ascending order
    """
    # Мой неправильный алгоритм
    """
    curr_max = max(origin_list)
    pos = origin_list.index(curr_max)
    n = 0
    while pos < len(origin_list) - 1:
        if origin_list[pos] > origin_list[pos + 1]:
            origin_list[pos], origin_list[pos + 1] = origin_list[pos + 1], origin_list[pos]
            pos += 1
        n -= 0
        curr_max = max(origin_list[:n])
        pos = origin_list.index(curr_max)
    print(origin_list)
    """
    # Правильное решение
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list) - n):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
        n += 1
    return origin_list


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

# Normal, task 3
# Сверялся с форком, но сделал в основном сам
def my_filter(cond, in_list):
    """
    Removes items from a list that don't satisfy a condition
    """
    for item in in_list:
        if not cond(item):
            in_list.remove(item)
    return in_list


my_list = ['', 'not null', 'bla', '', '10']
n = my_filter(len, my_list)
print(n)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# Normal, task 4
# Параллелограмм можно вычеслить по наличию двух пар параллельных линий.
# Чужой форк смотрел мельком, но сделал совсем по-другому
def slope_func (x1, y1, x2, y2):
    """
    Calculates the slope of a line
    """
    if x1 - x2 == 0:
        slope = float(inf)
    else:
        slope = (y1 - y2) / (x1 - x2)
    return slope


c_list = [[40, 8], [24, 33], [54, 33], [70, 8]]
slope_ab = slope_func(c_list[0][0], c_list[0][1], c_list[1][0], c_list[1][1])
slope_ac = slope_func(c_list[0][0], c_list[0][1], c_list[2][0], c_list[2][1])
slope_ad = slope_func(c_list[0][0], c_list[0][1], c_list[3][0], c_list[3][1])
slope_bc = slope_func(c_list[1][0], c_list[1][1], c_list[2][0], c_list[2][1])
slope_bd = slope_func(c_list[1][0], c_list[1][1], c_list[3][0], c_list[3][1])
slope_cd = slope_func(c_list[2][0], c_list[2][1], c_list[3][0], c_list[3][1])

if (slope_ab == slope_cd) or (slope_ac == slope_bd) or (slope_ad == slope_bc):
    print("This is a parallelogram!")
else:
    print("This is not a parallelogram.")
