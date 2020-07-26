number = input("Введите любое целое положительное число ")
number_int = int(number)
number_max = 0
number_tmp = 0
while(True):
    if((number_int == 0) or (number_tmp == 9)):
        break
    number_tmp = number_int % 10
    number_int = number_int // 10
    if(number_tmp > number_max):
        number_max=number_tmp
print(f"{number_max}")

