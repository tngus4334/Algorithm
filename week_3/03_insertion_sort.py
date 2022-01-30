input = [4, 6, 2, 9, 1]

# 1단계 : 4, 6, 2, 9, 1
#         <-
# 2단계 : 4, 6, 2, 9, 1
#         <-  <-
# 3단계 : 2, 4, 6, 9, 1
#         <- <-  <-
# 4단계 : 2, 4 ,6, 9, 1
#         <- <- <-  <-
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]: # 앞에있는숫자가 뒤에있는 숫자보다 크면
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1] # 변경
            else:
                break
            # print(i-j)
    return array


insertion_sort(input)
print(input)