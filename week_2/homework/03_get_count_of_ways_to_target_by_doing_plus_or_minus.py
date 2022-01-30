numbers = [2, 3, 1]
target_number = 0
# 1. +2 +3 +1 = 6       +++
# 2. +2 +3 -1 = 4       ++=
# 3. +2 -3 +1 = 0 -> 타켓+-+
# 4. +2 -3 -1 =-2       +--
# 5. -2 +3 +1 = 2
# 6. -2 +3 -2 = 0 -> 타겟
# 7. -2 -3 +1 = -4
# 8. -2 -3 -1 = -6
# 앞에있는 두 부호를 고정시키면 뒤에있는 것을 + 혹은 -로 바꾸면
# 두가지 경우의 수가 추가적으로 생긴다
# 마지막에 들어오는 새로운 원소를 뺄지 더할지에 따라 방법이 2가지 추가된다.
# n의 길이의 배열에서 더하거나 뺀 모든 경우의 수는
# n-1의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면됨

# [2, 3]
# 1. +2 +3 +1 = +2 +3 +1
#          -1 = +2 +3 -1
# 2. +2 -3 +1 = +2 -3 +1
#          -1 = +2 -3 -1
# 3. -2 +3 +1 = -2 +3 +1
#          -1 = -2 +3 -1
# 4. -2 -3 +1 = -2 -3 +1
#          -1 = -2 -3 -1


#numbers = [1, 1, 1, 1, 1]
#target_number = 3


result = [] # 모든 경우의 수 담기
# all_ways = result= []
# current_index = 0 현재 인덱스
# current_sum = 0
# 2, 3, 1


# target 숫자에 도달하는 방법이 아니라 모든 경우의 수를 출력하는 방법이기 때문에
def get_all_ways_to_by_doing_plus_or_minus(array, current_index, current_sum, all_ways):
    if current_index == len(array): # all_ways라는 배열에는 current_index값이 마지막에 도달했을때 끝내줘야함
        all_ways.append(current_sum) # 한칸 갈때마다 이 값을 +할것인지 -할것인지 넘겨주기때문
        return

    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum + array[current_index], all_ways) # 다음인덱스로 넘어가면서 두가지의 경우의 수가 생김
    # get_all_ways_to_by_doing_plus_or_minus(array, 1, 0 + 2, all_ways)
    get_all_ways_to_by_doing_plus_or_minus(array, current_index + 1, current_sum - array[current_index], all_ways)
    # get_all_ways_to_by_doing_plus_or_minus(array, 1, 0 - 2, all_ways)


print(get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result))
print(result)
# 그러나 우리가 원하는 것은 target을 만족한 것이 몇개나 있는지 찾아내는것 !