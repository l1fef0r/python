from itertools import cycle, count

print("Генерация целых чисел начиная с указанного, для выхода введите - 'q'")
try:
    for i in count(int(input('Введите стартовое число ')), 1):
        print(i)
        if input() == 'q':
            break

except:
    print("Где-то ошибка")

print("Повторение элементов списка, для выхода введите - 'q'")
list = input("Введите элементы списка, разделяя их пробелом ").split()

try:
    for item in cycle(list):
        if input() == 'q':
         break
        print(item)

except:
    print("Где-то ошибка")



