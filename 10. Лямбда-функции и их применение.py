def f1(x):
    return x**2 + 5


print(f1(1))

f2 = lambda x: x**2 + 5
print(f2(1))

a = -10
b = 1 if a >= 0 else -1  # Тернарный оператор
print(a, b)

a = [1, -1, 5, 0, -10, 20, 30, -15]
signs = lambda x: 1 if x > 0 else -1 if x < 0 else 0
# if x > 0:
#     return 1
# elif x < 0:
#     return -1
# else:
#     return 0
print([signs(elem) for elem in a])
print(map(signs, a))  # примени функцию sings к каждому элементу из a
print(list(map(signs, a)))

print([elem ** 2 for elem in a])
print(list(map(lambda x: x ** 2, a)))

##########

a = [1, -1, 5, 0, -10, 20, 30, -15]
print([elem if elem >= 0 else -elem for elem in a])
print(list(map(lambda x: x if x >= 0 else -x, a)))

print([elem for elem in a if elem >= 0])
print(list(filter(lambda x: x >= 0, a)))

##########

# TODO: изучить reduce
