input = "abcba"
# input = "tomato"

# is_palindrome(string) = 맨앞뒤 검사를 했다면 is_palindrome(string[1:-1]) 라는 함수로 축소가능

def is_palindrome(string): # is_palindrome("소주만병만주소")
    # is_palindrome("주만병만주")
    # is_palindrome("만병만")
    # is_palindrome("병") -> True
    if len(string) <= 1: # 한글자는 회문
        return True
    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])



print(is_palindrome(input))