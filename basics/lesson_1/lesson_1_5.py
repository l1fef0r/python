expens = int(input("Сколько фирма потратила?    "))
proceeds = int(input("Сколько фирма заработала?    "))
profit = False
if(proceeds > expens):
    print(f"В этом году мы в прибыли - {proceeds-expens} рубля(ей)\nНаша рентабельность составила {(proceeds-expens)/proceeds:.2f}")
    profit = True
elif(proceeds == expens):
    print("Мы на нуле")
else:
    print(f"В этом году мы плохо поработали - в минусе на {expens-proceeds} рубля(ей)")

if(profit == True):
    emplt = input("Сколько сотрудников в нашей организации? ")
    print(f"В этом году каждый сотрудник получит премию равную {(proceeds - expens)/int(emplt):.2f} рубля(ей)")
else:
    print("Поскольку мы отработали в минус, мы остались без премии")