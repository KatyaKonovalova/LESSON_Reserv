a = [i for i in range(5)]
b = [i**2 for i in range(7)]

for elem1, elem2 in zip(a, b):
    print(elem1, elem2)

print()

for i in range(len(b)):  # По индексам
    print(i, b[i])
print()

for elem in b:  # По элементам
    print(elem)
print()

for i, elem in enumerate(b):  # И по индексам, и по элементам
    print(i, elem)
