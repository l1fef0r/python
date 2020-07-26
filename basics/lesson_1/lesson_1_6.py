while(True):
    fresult = float(input("Какой результат спортсмена в первый день тренировок?    "))
    if(fresult>0): break
    else:
        print("Для того, чтобы улучшить результат нужно начать бегать!")
while(True):
    kmresult = float(input("Какой результат должен быть достигнут в километрах?    "))
    if(kmresult > 0): break
    else: print("Недостижимая цель!")

day = 1
while(True):
    print(f"{day}-й день: {fresult:.2f} км")
    if(fresult >= kmresult):
        break
    day += 1
    fresult = fresult * 1.1

print(f"\nНа {day}-й день тренировок спортсмен достиг результата - не менее {int(fresult)} км")

