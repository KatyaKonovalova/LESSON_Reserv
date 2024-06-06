a = [1, 2, 3]
b = a
c = a.copy()
print(a, b, c)

a[0] = 10
print(a, b, c)

print(id(a), id(b), id(c))

a = [1, 2, 3, [4, 6]]
b = a.copy()  # Поверхностная копия (копируются ссылки на объекты, а не сами объекты)
print(a, b)

a[3][0] = 40
a[0] = 10
print(a, b)


def f(elem, a=[]):  # Пустой список задается всего один раз - при инициализации функции
    a.append(elem)
    return sum(a)


data = [1, 2, 3]
print(f(4, data.copy()))
print(data)
print()
print(f(4, data))
print(data)
print()
print(f(5))
print(f(6))


def f1(elem, a=None):
    if a is None:
        a = []
    # return f2
    a.append(elem)
    return sum(a)


def f2():
    return 10


print()
print(f1(5))
print(f1(6))
