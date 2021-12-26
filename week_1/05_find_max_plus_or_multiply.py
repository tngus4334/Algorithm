input = [0, 3, 5, 6, 1, 2, 4]


# 4 + 1, 4 * 1
# 숫자를 돌면서 나온 각각의 숫자가 1보다 작거나 같다면
# 더해버리는게 낫고 1보다 크다면 곱해보는게 낫다

def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        # 더해진 합계가 1보다 작거나 같아도 +해줘야함
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number

    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)
