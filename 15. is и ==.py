a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # Сравнение ссылок на объект в памяти
print(a == b)  # Сравнение описано в магическом методе __eq__(self, other)

print()

# Числа от -5 до 256 включительно интернированы, т.е. заранее заданы и переменные ссылаются на них

a = 100
b = 100
print(a is b)

print()

a = 1000
b = 1000
print(a is b)  # TODO: почему в консоли Python выводит False, а в PyCharm - True?

# https://www.dev-notes.ru/articles/python/is-identity-vs-equality/
