from itertools import count
from math import factorial

def fact():
    for el in count(0):
        yield factorial(el)

print("Программа последовательно увеливает число на еденицу для расчета его факториала, введите q для выхода ")
a = 0
for i in fact():

    if input() == 'q':
        break
    print(f"Факториал {a} = {i}")
    a+=1


