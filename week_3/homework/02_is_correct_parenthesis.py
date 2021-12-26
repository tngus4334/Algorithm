input = "(())()"


def is_correct_parenthesis(string):
    stack = []

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)  # 여기 아무런 값이 들어가도 상관없음! ( 가 들어가있는지 여부만 저장해둔것
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            stack.pop()

    if len(stack) != 0:
        return False
    else:
        return True


print(is_correct_parenthesis(input))