class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police  = is_police
    def Go(self):
        print(f"Машина {self.name} поехала")
    def Stop(self):
        print(f"Машина {self.name} остановилась")
        self.speed = 0
    def Turn(self, direction):
        print(f'Машина {self.name} повернула на{"лево" if direction == False else "право"}')
    def ShowSpeed(self):
        print(f"Текущая скорость автомобиля равна {self.speed}")


class TownCar(Car):
    def ShowSpeed(self):
        print(f"Текущая скоросчть автомобиля {self.name} равна {self.speed}")
        if (self.speed >= 60):
            print("Скорость превышена!!")

class SportCar(Car):
    '''спорткар'''

class WorkCar(Car):
    def ShowSpeed(self):
        print(f"Текущая скорость автомобиля {self.name} равна {self.speed}")
        if(self.speed >= 40):
            print("Скорость превышена!!")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


police_car = PoliceCar(120, "white", "Policecar")


town_car = TownCar(100, "white", "Niva")
town_car.Go()
town_car.Turn(True)

work_car = WorkCar(30, "black", "Gruzovik")
work_car.Go()
work_car.Turn(False)
work_car.Stop()
work_car.ShowSpeed()

town_car.ShowSpeed()