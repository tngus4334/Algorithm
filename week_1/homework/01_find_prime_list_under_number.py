input = 20


# 소수는 자기자신과 1 외에는 아무것도 나눌 수 없음
# 주어진 자연수 N이 소수이기 위한 필요충분조건은
# N이 N의 제곱근보다 크지않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데 몫과 나누는 수 둘 중 하나는
# 반드시 N의 제곱근 이하
def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):
        # n을 20이라고 한다면
        # i를 2 3 5 7 9 11.. 19
        # 2 ~ n - 1 증에서 소수인 친구들만
        for i in prime_list:  # i의 범위  : 2부터 n-1 이하의 소수
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
