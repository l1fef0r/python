class CheckError:
    @staticmethod
    def isnotstring(my_list):
        while True:
            inp = input('Введите значения и нажимайте Enter - ')
            if (inp == ('stop' or 'стоп')): break

            if inp.isdigit():
                my_list.append(inp)
            else:
                try:
                    my_list.append(f"{float(inp)}")
                except:
                    print("Недопустимое значение - строка или булево")
            print(f"Текущее содержимое списка: {my_list}")
            print('Напишите "stop" для прекращения ввода')
        return my_list

my_list = [] #С целью дополнить список
my_list = CheckError.isnotstring(my_list)
# Не сообразил как сделать изящно, если бы пайтон не возвращал всегда "None",
# в случае не прохождения проверки, иначе он будет добавлять None в список
