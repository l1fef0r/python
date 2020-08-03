def my_func_with_while(x, y):
    i = 1
    x_pow = x
    while i < abs(y):
        x_pow *= x
        i += 1

    return (1/x_pow)

def my_func(x, y):
    return 1/(x ** y)
x, y = input("Напишите через проблем какое число и в какую степень необходимо возвести, причем степень должна быть отрицательной ").split()
print(f"{x} в степени -{abs(int(y))} будет равен {float(my_func_with_while(int(x), int(y)))} с использованием цикла")
print(f"{x} в степени -{abs(int(y))} будет равен {float(my_func(int(x), abs(int(y))))} без использования цикла")

