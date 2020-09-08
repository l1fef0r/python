import time
import itertools


class TrafficLight:
    __color = [["red", 7], ["yellow", 2], ["green", 7], ["yellow", 2]]
    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r{light[0]}", end = "")
            time.sleep(light[1])



trafficlight = TrafficLight()
trafficlight.running()
