with open("numbers.txt", 'w', encoding='utf-8') as file2:
        file2.write(input("Напишите набор чисел разделенных пробелами "))
file2.close()


with open("numbers.txt", "r", encoding="utf-8") as file:

        result = file.read().split()
        result_int = 0

        for i in result:
                result_int += int(i)

        print(result_int)
file.close()