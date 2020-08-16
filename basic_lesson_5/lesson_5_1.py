with open("text2.txt", 'w', encoding='utf-8') as file:
    while True:
        line = input("Введите строку, либо нажмите энтер для выхода ")
        if not line:
            break
        file.write(line + '\n')
