a = [1, 2, 3]
a.append(a)
print(a)
print(a[0])
print(a[3][3][3][3][3][3])


def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(5))
