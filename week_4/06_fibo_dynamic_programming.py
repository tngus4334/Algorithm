# 1. 만약 메모에 있으면 그 값을 바로 반환하고
# 2. 없으면 아까 수식대로 구한다.
# 3. 그리고 그 값을 다시 메모에 기록한다.

input = 100

memo = {
    1: 1,
    2: 1
}


# Fibo(100) -> Fibo(99) -> Fibo(98) .... 위에서 Top Down
# Fibo(1) -> Fibo(2) -> Fibo(30) .... Bottom up
def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo: # n이 fibo_memo에 있으면
        return fibo_memo[n] # 바로 반환

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo) # n번째 피보값 구하기
    fibo_memo[n] = nth_fibo # fibo_memo에 값저장

    return nth_fibo


print(fibo_dynamic_programming(input, memo))
