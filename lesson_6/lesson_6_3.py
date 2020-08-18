class Worker:
    _income = {"wage": "wage", "bonus": "bonus"}
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    def get_total_income(self):
        return f"{sum(self._income.values())}"

worker = Position("Ivan", "Ivanov", "plamber", 10000, 20000)
print(worker.get_full_name())
print(worker.get_total_income())
