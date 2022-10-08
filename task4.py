# Задана наткральная степень K. Сформировать случайным образом
# список коэффицентов (от 0 до 10) многочлена, записать в файл полученный многочлен
# не менее 3-х раз.

from random import randint, choice




def int_input():
    while True:
        try:
            result = abs(int(input('Введите натуральную степень: ')))
        except ValueError:
            print("Ошибка, повторите ввод")
        else:
            return result
k = int_input()


def make_polynom(k):
    str_list = [str(randint(1,10))+ "x^"+ str(k)]
    while k != 2:
        k -=1
        str_list += [str(randint(0,10))+ "x^"+ str(k)]
    str_list += [str(randint(0,10)) + "x"] 
    for i in str_list:
        if i[0] == "0":
            str_list.remove(i)
    str_list += [str(randint(1,10))]
    return str_list
str_list = make_polynom(k)
polynom = ""
for i in str_list:
    polynom += i + choice([" + ", " - "])
    my_polynom = polynom[:-2] + "= 0"

print(my_polynom)    

with open('file.txt', 'a') as data:
        data.write(my_polynom)
        data.write("\n")
    

