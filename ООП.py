class Cat:
    def __init__(self, name, color, eye_color):  # Конструктор класса
        self.name = name
        self.color = color
        self.eye_color = eye_color

    def meow(self):
        print(f'Cat {self.name} meow!')

    @staticmethod
    def meow2():
        print('Все коты умеют мяукать')


cat1 = Cat('Knight', 'blue', 'brown')
cat2 = Cat('Knight2', 'white', 'green')

print(cat1.name, cat1.color, cat1.eye_color)
print(cat2.name, cat2.color, cat2.eye_color)
cat1.meow()
cat2.meow()

Cat.meow(cat1)
Cat.meow2()
cat1.meow2()

a = int(5)  # int - это не функция, а вызов конструктора класса int
