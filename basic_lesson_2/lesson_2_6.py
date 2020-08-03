
goods = []

features = {"название": "", "цена": "", "количество": "", "ед": ""}
analytics = {"название": [], "цена": [], "количество": [], "ед": []}

n = 0
while(True):
    if input("Для выхода из программы напишите end: ").upper() == "END":
        break
    n = +1
    for f in features.keys():
        val = input(f"Введите значение свойства _{f}_ нового товара: ")
        features[f] = int(val) if (f == "цена" or f == "количество") else val
        analytics[f].append(features[f])
        goods.append((n, features))
    print(f"\nТекущая аналитика по товарам\n")
    for key, val in analytics.items():
        print(f"{key}: {val}")
    print("\n")
