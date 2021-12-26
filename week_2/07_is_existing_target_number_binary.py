finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]
# 이진탐색은 일정한 규칙으로 정렬된 데이터일때만 사용가능 -> 이진탐색하려면 정렬해야함

def is_exist_target_number_binary(target, numbers):
    current_min = 0
    current_max = len(numbers) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if numbers[current_guess] == target:
            return True
        elif numbers[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2
    return False



result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)