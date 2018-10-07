# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# Easy, task 1
# Задание понял в том смысле, что округлить до кол-ва знаков после зяпятой.
# Алгоритм подсмотрел на чужом форке, сделал по аналогии
def my_round(number, ndigits):
    """
    Rounds number to ndigits after the decimal separator
    """
    out_number = number * (10 ** ndigits)
    num_str = str(out_number)
    pos_of_dec = num_str.find('.')
    if num_str[pos_of_dec + 1] in ['5', '6', '7', '8', '9']:
        out_number += 1
    out_number = out_number // 1
    out_number = out_number / (10 ** ndigits)
    return out_number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# Easy, task 2
def lucky_ticket(ticket_number):
    """
    Checks whether a ticket_number is a lucky one.
    """
    tn_str = str(ticket_number)
    tn_int_list = list(map(int, tn_str))

    if len(tn_str) != 6:
        return "There aren't 6 digits in your ticket number."
    else:
        first_half = sum(tn_int_list[:3])
        second_half = sum(tn_int_list[3:])
        if first_half == second_half:
            return "Your ticket is a lucky one!"
        else:
            return "It's just a regular ticket"


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
