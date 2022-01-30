# Fibo(N) = Fibo(N-1) + Fibo(N-2)
# Fibo(1) = Fibo(2) = 1

input = 20


def fibo_recursion(n):
    if n == 1 or n == 2:
        return 1

    return fibo_recursion(n - 1) + fibo_recursion(n - 2)


print(fibo_recursion(input))
