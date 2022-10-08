# Вычислить число с заданной точностью d


def float_input():
    while True:
        try:
            result = float(input('Введите число: '))
        except ValueError:
            print("Ошибка, повторите ввод")
        else:
            return result

n = float_input()

def acc_input():
    while True:
        try:
            result = float(input('Введите точность (например: 0.0001): '))
        except ValueError:
            print("Ошибка, повторите ввод")
        else:
            return result

accuracy = acc_input()

def num_with_accuracy(n, acc):
    if acc % 1 != 0:
        count = len(str(acc)) - len(str(int(acc))) - 1
        new_n = round(n, count)
    else:
        new_n = int(n)
    if n % 1 == 0: 
        new_strn = str(new_n) + (count - 1) * '0'
        return new_strn
    return new_n

print("число", n, "c точностью", accuracy, "равно", num_with_accuracy(n,accuracy))