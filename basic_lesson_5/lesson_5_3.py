staff = {}
with open("staff", "r", encoding="utf-8") as file:
    for l in file:
        words = l.split()
        staff[words[0]] = float(words[1])


sum = 0
for key, value in staff.items():
    sum += value
    if(value<20000): print(key)

print(f"Средняя зарплата сотрудников равна {value/len(staff)}")

