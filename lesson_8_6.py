class Warehouse:
    def __init__(self, number, l, w, h):
        self.number = number
        self.length = l
        self.width = w
        self.height = h
        self.equipments_amount = 0
        self.equipments = []


    def get_nubmer(self):
        return self.number

    def read_equipments(self):
        for i in self.equipments:
            print(f"{i.getName()} {self.number}")

    def set_equipments_list(self, equipments):

        while equipments:
            self.equipments.append(equipments[0])
            self.equipments_amount += 1
            del equipments[0]

    def set_equipment(self, equipment, warehouse_number):
        self.number = warehouse_number
        self.equipments_amount += 1
        self.equipments.append(equipment)

    def get_equipments(self, name_equipment, amount):
        eqfortrans = []
        numberforeq = []
        n = 0
        # обработка исключения, обратка количества товара
        try:
            for i in self.equipments:
                if len(numberforeq) >= int(amount):
                    break

                if i.name == name_equipment:
                    numberforeq.append(n)
                n += 1

            if len(numberforeq) < int(amount):
                print(f"Нет достаточного количества {name_equipment} на складе №{self.number}")

            numberforeq.reverse()
            for i in numberforeq:
                eqfortrans.append(self.equipments.pop(i))
                self.equipments_amount -= 1
        except:
            print("Проверьте ввод сканер/принтер/ксерокс, а также нужно вводить количество в ввиде числа")
        return eqfortrans

class Equipment:
    def __init__(self, producer, serial_number, name):

        self.producer = producer
        self.serial_number = serial_number
        self.name = name

    def getName(self):
        return self.name, self.producer, self.serial_number


class Printer(Equipment):
    def __init__(self, producer, serial_number, name = "принтер"):
        super().__init__(producer, serial_number, name)
        self.name = name
    def Type(self):
        print(f"{self.name} {self.serial_number} печатает")

class Scanner(Equipment):
    def __init__(self, producer, serial_number, name = "сканер"):
        super().__init__(producer, serial_number, name)
        self.name = name
    def Scan(self):
        print(f"{self.name} {self.serial_number} cканирует")

class Copier(Equipment):
    def __init__(self, producer, serial_number, name = "ксерокс"):
        super().__init__(producer, serial_number, name)
        self.name = name
    def Copy(self):
        print(f"{self.name} {self.serial_number} копирует")


war1 = Warehouse(1, 40, 30, 25)
# возможно как-то имеет смысл сделать уникальное присвоение номера для склада,
# чтобы не было возможности сделать один и тот же для нескольки экземпляров
war2 = Warehouse(2, 40, 30, 25)



print('Есть два склада (1, 2), оборудование типа принтер, сканер, ксерокс. Заполните список оборудования. Попробуйте переносить оборудование из одного в другой')

my_list = []
value = True
while True:
    eq = None
    if (value == True):
        print("Введите тип (сканер/принтер или ксерокс), задайте серийный номер и определите производителя (например HP, samsung и т.п.)")
        inp = input("scanner/printer/copier? или введите 'stop' для выхода ")
        if (inp == 'stop'):
            break
        elif (inp == 'scanner' or inp == 'scan' or inp == 's' or inp == 'sc'):
            eq = Scanner(input("введите производителя "), int(input("введите серийный номер(целочисленное) ")))
            my_list.append(eq)
            value = False
        elif (inp == 'printer' or inp == 'print' or inp == 'pr' or inp == 'p'):
            eq = Printer(input("введите производителя "), int(input("введите серийный номер(целочисленное) ")))
            my_list.append(eq)
            value = False
        elif (inp == 'copier' or inp == 'cop' or inp == 'co' or inp == 'c'):
            eq = Copier(input("введите производителя "), int(input("введите серийный номер(целочисленное) ")))
            my_list.append(eq)
            value = False
        else:
            value = True
            print("Похоже вы ошиблись в вводе данных")

    if (value == False):
        var = int(input("В какой склад разместить оборудование? 1 или 2 "))
        if (var == 2):
            war2.set_equipment(eq, var)
            value = True
        elif (var == 1):
            war1.set_equipment(eq, var)
            value = True
        else:
            print("Похоже вы ошиблись в вводе данных/товар обязательно нужно разместить на склад! 1 или 2")

print("текущее количество товара на складах")
war2.read_equipments()
war1.read_equipments()

print("Если потребуется перенести товар со склада на склад укажите номер склада и какой товар хотите перенести, или напишите stop, когда закончите перенос")

my_w = [war1, war2] #пример того что можно использовать любое количество складов
while True:
    fromW = input("С какого склада взять?/для выхода впишите stop ")
    if(fromW == 'stop'): break

    name_equipment = input("Наименование товара, вводить надо  сканер/принтер/ксерокс ")
    amount = input("его количество = ")

    n = 0
    for i in my_w:
        if (int(fromW) == i.get_nubmer()):
            list_eq = i.get_equipments(name_equipment, amount)
            toW = int(input("На какой склад передать? "))

            nn = 0
            for ii in my_w:
                if (toW == ii.get_nubmer()):
                    ii.set_equipments_list(list_eq)
                    break
                if (nn == len(my_w) - 1):
                    print("Нет склада КУДА хотите передать, проверьте правильность ввода")
                nn += 1
            break
        if (n == len(my_w)-1):
            print("Нет склада ОТКУДА хотите взять, проверьте правильность ввода")
        n += 1

for i in my_w:
    i.read_equipments()