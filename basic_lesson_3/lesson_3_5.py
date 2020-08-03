import re
numbers = input("Введите числа через пробел ")
list_numbers = numbers.split()
print(list_numbers)

sum = 0
for i in list_numbers:
    sum = sum + int(i)
print(f"Сумма чисел равна {sum}")

while True:
    if("YES" == input("Хотите продолжить ввод чисел? напишите Yes ").upper()):
        new_numbers = input("Продолжите ввод чисел через пробел ")
        new_list_numbers = new_numbers.split()
        numbers = numbers + " " + new_numbers
        print(numbers)

        for i in new_list_numbers:
            if (re.search('[^0123456789]',i)):
                print(f"Специальный символ или буква {i}!!!")
                break

            sum = sum + int(i)

        print(f"Сумма чисел равна {sum}")

    else: break

print(f"Итоговая сумма чисел равна {sum}")
