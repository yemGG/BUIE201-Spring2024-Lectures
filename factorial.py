def g():
    pass

def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    g()
    return n * factorial(n-1)

def factorial_it(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


x = factorial(3)
print (x)