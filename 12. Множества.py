# Множество - это изменяемая неупорядоченная коллекция, содержащая неповторяющиеся объекты
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)
print(a | b)
print(a ^ b)
print(a - b)
print(a < b)

print({1, 2, 3} < {1, 2, 3, 4, 5})
print({1, 2, 3} < {1, 2, 3})
print({1, 2, 3} <= {1, 2, 3})

for elem in a:
    print(elem)

# Объекты словаря должны быть неизменяемыми,
# т.к. для того, чтобы гарантировать уникальность элементов, он их хэширует

# Аналогично ключи в словарях не могут быть изменяемыми,
# т.к. они тоже хэшируется, обеспечивая уникальность

# Также благодаря хэшированию поиск объектов имеет сложность O(1)

print()
print(hash(1))
print(hash('1'))
# print(hash([1]))  - TypeError: unhashable type: 'list'

# a = {[1, 2]}  - будет ошибка TypeError: unhashable type: 'list'
# print(a)
