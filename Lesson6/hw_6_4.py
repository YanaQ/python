# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
# name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return f'Автомобиль поехал'
    def stop(self):
        return f'Автомобиль остановился'
    def turn_left(self):
        return f'Автомобиль повернул налево'
    def turn_right(self):
        return f'Автомобиль повернул направо'
    def show_speed(self):
        return f'Текущая скорость автомобиля марки {self.name} {self.speed} км/ч'

class TownCar(Car):
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family
    def show_speed(self):
        print(f'Текущая скорость автомобиля марки {self.name} {self.speed} км/ч')
        if self.speed > 60:
            print('Вы превысили скорость!')
        else:
            print('Вы едете с нормальной скоростью')

class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
class WorkCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
    def show_speed(self):
        print(f'Текущая скорость автомобиля марки {self.name} {self.speed} км/ч')
        if self.speed > 40:
            print('Вы превысили скорость!')

class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

ford = TownCar('Toyota', 70, 'black')
print(ford.name, ford.speed, ford.color)
ferrary = SportCar('Ferrary', 180, 'red')
print(ferrary.name, ferrary.speed, ferrary.color)
audi = WorkCar('Audi', 30, 'white', True)
print(audi.go(), audi.turn_left(), audi.stop())
police = PoliceCar('Ford', 120, 'red')
print(ford.show_speed())
print(ferrary.show_speed())
print(audi.show_speed())
print(police.show_speed())

