# Даны два файла, в каждом из которых находится
# запись многочленов. Задача - сформировать файл,
# содержащий сумму многочленов.

with open('poly_1.txt', 'r') as data:
        result1 = data.read()
c_result1 = result1.split("=")
with open('poly_2.txt', 'r') as data:
        result2 = data.read()

sum_result = c_result1[0] + " + " + result2 
print(sum_result)
    
with open('sum_poly.txt', 'a') as data:
        data.write(sum_result)