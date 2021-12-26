input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for element in array:  # array의 길이만큼 아래 연산이 실행된다.
        if number == element: # 비교연산 1번 실행
            return True # N * 1 = N 만큼의 시간복잡도
    return False


result = is_number_exist(3, input)
print(result)
