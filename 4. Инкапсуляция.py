# Инкапсуляция - скрытие данных
# public - публичный доступ, т.е. виден везде
# _protected - защищенный доступ, виден внутри класса и в его потомках.
# Однако снаружи тоже видно, но есть предупреждение, что не стоит так изменять и читать
# __private - приватный доступ, т.е. виден только внутри класса

# Для безопасного получения данных используются так называемые геттеры и сеттеры
# В Python они же называются property и prop.setter


class Cat:
    def __init__(self, name, color):
        self.name = name
        self._color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if isinstance(color, str):
            self._color = color
        else:
            raise TypeError('color must be str')


cat1 = Cat('Bob', 'white')
print(cat1.name)
cat1.color = 'black'
print(cat1.color)
