input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array) # O(N^2)
    for i in range(n - 1): # array의 길이
        # -1 : 한번은 맨 마지막에 비교를 하지 않아도됨
        # i : i만큼 반복하면서 맨 뒤에 것이 정렬이 되었기 때문에 빼줘도 됨 -> n-i-1
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return


bubble_sort(input)
print(input)