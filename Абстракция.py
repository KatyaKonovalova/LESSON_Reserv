from abc import ABC


class Car(ABC):
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        return self.speed


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')


class PoliceCar(Car):
    pass
