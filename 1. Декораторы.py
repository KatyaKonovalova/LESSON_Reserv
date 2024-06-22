def f1(func):
    return func()


def f2():
    return 10


print(f1(f2))
print(f2)

#########

@f1
def f3():
    return 10


print(f3)


##########


def f4(func):

    def f5(arg):
        return func(arg ** 2)

    return f5


@f4
def f6(n):
    return n


print(f6(5))


###########
print()
a = 35


def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(a))


def g1(func, res={}):

    def g0(n):
        if n in res:
            return res[n]
        res[n] = func(n)
        return res[n]

    return g0


@g1
def fib2(n):
    if n < 2:
        return 1
    return fib2(n - 1) + fib2(n - 2)


print(fib2(a))
