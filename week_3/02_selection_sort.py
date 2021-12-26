input = [4, 6, 2, 9, 1]


#for i in range (5 - 1): # 맨 마지막 하나남은 원소는 비교하지 않음
#    for j in range (5 - i):
#        print(i + j)

def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!