def my_func(arg1, arg2, arg3):
    if(arg1 >= arg2 >= arg3):
        return arg1 + arg2
    elif(arg1 >= arg3 >= arg3):
        return arg1 + arg3
    else: return arg2 + arg3

while True:
    if("END" == input("напишите end если хотите завершить работу прогораммы ").upper()): break
    a, b, c = input("Напишите три числа через пробел ").split()
    print(f"Сумма двух наибольших чисел будет равна  {my_func(int(a), int(b), int(c))}")