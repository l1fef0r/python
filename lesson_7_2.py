from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, size):
            self.size = size

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption

class Coat(Clothes):

    @property
    def consumption(self):

        cons = round(self.size/6.5) + 0.5
        print(f"Sewing a coat - {cons}")
        return cons

class Costume(Clothes):
    @property
    def consumption(self):
        cons = (2*self.size + 0.3)/100
        print(f"Sewing a costume - {cons}")
        return cons

coat1 = Coat(int(input("Введите размер польто для расчета количества необходимой ткани ")))
print(f"Вам потребуется {coat1.consumption} метров ткани для польто")
costume1 = Costume(int(input("Введите размер костюма для расчета количества необходимой ткани ")))
print(f"Вам потребуется {costume1.consumption} метров ткани для для костюма")

print(f"Всего вам потребуется {coat1 + costume1} метров ткани")