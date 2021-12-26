input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array) # O(N^2)
    for i in range(n - 1): # n의 길이
        for j in range(n - i - 1): # n의 길이
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return


bubble_sort(input)
print(input)