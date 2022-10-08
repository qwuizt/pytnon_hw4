# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

def int_input():
    while True:
        try:
            result = abs(int(input('Введите натуральное число: ')))
        except ValueError:
            print("Ошибка, повторите ввод")
        else:
            return result

n = int_input()

def simple_multipliers(n):
    my_list = []
    m = 2
    while m  <= n:
        if n % m == 0:
            my_list.append(m)
            n //= m
        else:
            m += 1
    return my_list
print(simple_multipliers(n))