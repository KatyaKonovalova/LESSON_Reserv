import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.__matrix = matrix
        self.dtype = type(matrix[0][0])

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            a = []
            for i in range(len(self.__matrix)):
                a.append([0] * len(self.__matrix[0]))
                print(a)
                for j in range(len(self.__matrix[0])):
                    a[i][j] = self.__matrix[i][j] * other
            return Matrix(a)
        raise TypeError('Умножение возможно только на число')

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        result = '['
        for line in self.__matrix:
            result += '[' + ' '.join([str(elem) for elem in line]) + ']\n'
        return result[:-1] + ']'

    def __repr__(self):
        return f'Matrix({self})'  # str(self)

    def __call__(self, *args, **kwargs):
        return 'Был вызван метод call'


a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Кортеж - не разрешает изменять данные, добавлять и удалять
# Массив - не разрешает добавлять и удалять
# Список - разрешает все

# Массив - это структура данных конкретного размера, состоящая из элементов одного типа данных
# Списки в отличие от массивов можно увеличивать (append, extend) и уменьшать (pop, remove)

# print(a * 2)
# print([a * 2])
#
# b = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# print(b * 2)
# print([b * 2])


c = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

# print(c * 2)
# print(str(c * 2))
# print([c * 2])
# print(c.dtype)
# print(2 * c)
try:
    print(c * 2)
except TypeError:
    print('Произошла ошибка типов данных')
# print(c())
