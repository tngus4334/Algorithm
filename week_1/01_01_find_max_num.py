input = [3, 5, 6, 1, 2, 4]

#find_max_num을 다른 숫자들과 비교하는 방식으로 푼다.
def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)
