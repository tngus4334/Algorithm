# factorial(N) = N * factorial(N-1)
# ....
# factorial(1) = 1

# 5 * factorial(4) .....
def factorial(n):  # 5
    if n == 1:  # 5 == 1? X
        return 1

    return n * factorial(n - 1)  # 5 * factorial(4)


print(factorial(5))
