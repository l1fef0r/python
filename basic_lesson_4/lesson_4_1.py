from sys import argv
print("Здесь расчет заработной платы сотрудника")
name, worked, wage, bonus = argv
print(argv)
try:
    print(f"Заработная плата сотрудника равна {int(worked)*int(wage)+int(bonus)}")
except:
    print("Все параметры должны быть ведены ввиде числа")