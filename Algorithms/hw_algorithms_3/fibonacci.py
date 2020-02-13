
def fibonacci(n):
    fib_1 = 1
    fib_2 = 1
    i = 0
    if n == 1:
        return fib_1
    if n == 2:
        return fib_2

    while i < n - 2:
        fib_total = fib_1 + fib_2
        fib_1, fib_2 = fib_2, fib_total
        i += 1
    return fib_total

print(fibonacci(8))



