# Метод index в списках и строках
# Полиморфизм - один и тот же метод реализован в несвязанных друг с другом классах

class Animal:
    def __init__(self, name):
        self.name = name

    def forward(self):
        print('Бежит вперед')


class Transport:
    def __init__(self, name):
        self.name = name

    def forward(self):
        print('Двигается вперед')


cat = Animal('cat')
bus = Transport('bus')
cat.forward()
bus.forward()
