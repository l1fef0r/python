def func(num_1, num_2):
    return num_1/num_2 if(num_2 != 0) else "Деление на ноль!"


while True:
    if(input("Enter if you want continue or write end if you want to stop process ").upper() == "END"): break
    a, b = input("You have to write number through space: ").split()
    a = int(a)
    b = int(b)
    print(func(a, b))