class Cell():
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        if (self.amount - other.amount) < 0:
            return "Ячеек второй клетки больше ,вычитанипе не возможно"
        return Cell(self.amount - other.amount) if self.amount - other.amount > 0 else self

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(self.amount / other.amount)

    def make_oder(self, rows):
        str = self.amount // rows
        str2 = self.amount % rows

        return '\n'.join(['*'*rows for _ in range(str)]) + '\n' + str2*'*' + '\n'


cell1 = Cell(28)
cell2 = Cell(37)

print(cell1.make_oder(5))
print(cell2.make_oder(5))

cell1 = cell1 + cell2

print(cell1.make_oder(10))

