class Stationary:
    def __init__(self, tittle ="a thing for drawing"):
        self.tittle = tittle
    def draw(self):
        print(f"Start draw by {self.tittle}")

class Pen(Stationary):

    def draw(self):
        print(f"Start draw with pen by {self.tittle} ")

class Pencil(Stationary):

    def draw(self):
        print(f"Start draw with pencil by {self.tittle}")

class Marker(Stationary):

    def draw(self):
        print(f"Start draw with marker by {self.tittle}")

stat = Stationary()
stat.draw()

pen = Pen("Ruchka")
pen.draw()
pencil = Pencil("Karandash")
pencil.draw()
marker = Marker("Marker")
marker.draw()