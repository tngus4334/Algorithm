input = "abcba"
# input = "tomato"



def is_palindrome(string):
    n = len(string)
    for i in range(n): # i는 0부터 n-1까지 반복된다
        if string[i] != string[n - 1 - i]: # 인덱스이기 때문에 맨 뒤에있는게 n-1, i는 0부터 시작함
            return False

    return True


print(is_palindrome(input))