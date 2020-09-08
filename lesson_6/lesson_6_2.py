class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def Mass_for_Road(self):

        return self._length*self._width*int(input("введите массу в килограммах "))*int(input("введите толщину дорожного полотна "))


road_1 = Road(10, 10)

print(road_1.Mass_for_Road())