dicte = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
dictr = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}
result = []
with open("dict.txt", "r", encoding="utf-8") as file:
    for l in file:
        result.append(l.split()[0])


for i in range(0, len(result)):
    print(f"{dicte.get(result[i])} - {i+1}")

with open("dict2.txt", 'w', encoding='utf-8') as file2:
    for i in range(0, len(result)):
        print(f"{dicte.get(result[i])} - {i + 1}")
        file2.write(f"{dicte.get(result[i])} - {i + 1}\n")