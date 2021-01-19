class Warehouse:
    def __init__(self, number, l, w, h):
        self.number = number
        self.length = l
        self.width = w
        self.height = h

    def get_nubmer(self):
        return self.number

class Equipment:
    def __init__(self, warehouse, producer, serial_number):
        self.warehouse_number = warehouse.get_nubmer()
        self.producer = producer
        self.serial_number = serial_number


class Printer(Equipment):
    def __init__(self, warehouse, producer, serial_number, name):
        super().__init__(warehouse, producer, serial_number)
        self.name = name
    def Type(self):
        print(f"{self.name} {self.serial_number} печатает")

class Scanner(Equipment):
    def __init__(self, warehouse, producer, serial_number, name):
        super().__init__(warehouse, producer, serial_number)
        self.name = name
    def Scan(self):
        print(f"{self.name} {self.serial_number} cканирует")

class Copier(Equipment):
    def __init__(self, warehouse, producer, serial_number, name):
        super().__init__(warehouse, producer, serial_number)
        self.name = name
    def Copy(self):
        print(f"{self.name} {self.serial_number} копирует")

war = Warehouse(1, 40, 30, 25)
cop = Copier(war, "HP", 2, "принтер")
cop.Copy()