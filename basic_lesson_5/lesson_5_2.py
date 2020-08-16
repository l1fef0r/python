count = 0
with open("text.txt", "r", encoding="utf-8") as file:
    for l in file:
        count+=1
        words = l.split()
        print(f"Количество слов в строке {count} = {len(words)}")
    print(f"Количество строк равно {count}")