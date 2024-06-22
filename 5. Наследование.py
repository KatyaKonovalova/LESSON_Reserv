
class Animal:
    def __init__(self, name, color):
        self.name = name
        self._color = color

    def sound(self):
        print('Издает звук')


class Dog(Animal):
    def __init__(self, name, color, breed):
        super().__init__(name, color)
        self.__breed = breed

    # Пример переопределения родительского метода (override)
    def sound(self):
        print('Гавкает')


animal = Animal('animal', 'blue')
dog = Dog('dog', 'yellow', 'breed1')
animal.sound()
dog.sound()
