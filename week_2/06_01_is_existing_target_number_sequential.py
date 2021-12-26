finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


# O(N) 시간복잡도

def is_existing_target_number_sequential(target, array):
    find_count = 0  # 이 함수가 몇번이나 실행되는가
    for number in array:
        find_count += 1  # for 문을 실행할 때 find_count를 1씩 증가
        if target == number:
            print(find_count)  # return true를 하는 순간
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True
