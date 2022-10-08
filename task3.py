# Задайте последовательность чисел. Напишите программу которая составит список
# простых множителей числа N.



my_list = [1,11,11,9,9,0,9,2]
print("Исходный список:", my_list)
new_list = []
del_list = []
for e in my_list:
    if e not in new_list:
        new_list.append(e)    
    else:
        del_list.append(e)
for i in del_list:
        if i in new_list:
            new_list.remove(i)
print("отформатированный список:", new_list)