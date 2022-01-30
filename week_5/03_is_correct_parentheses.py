# 균형잡힌 괄호 문자열 -> 올바른 괄호 문자열
# 올바른 괄호 문자열 ? 어떻게 알았지?

from collections import deque

balanced_parentheses_string = "()))((()"


def is_correct_parenthesis(string):  # 올바른 괄호문자열인지 확인
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
    return len(stack) == 0

def reverse_parenthesis(string):
    reversed_string = ""  # u를 뒤집은거 저장
    for char in string:
        if char == '(':
            reversed_string += ')'
        else:
            reversed_string += '('
    return reversed_string


def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""
    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break  # u가 균형잡힌 괄호 문자열이 안되게 하려면 더이상 쌍이 안생기도록 해야함
    v = ''.join(list(queue))
    return u, v

# 1. 입력이 빈 문자열인 경우 빈 문자열 반환
def change_to_correct_parenthesis(string):  # 균형잡힌 괄호문자열을 올바른 괄호 문자열로 바꾸는 것
    if string == "":
        return ""
    # 2. 문자열 w를 두 "균형잡힌 괄호문자열" u,v로 분리
    # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며
    # v는 빈 문자열이 될 수 있습니다.
    # (와 )의 개수가 같아야한다
    # print(u,v)
    u, v = separate_to_u_v(string)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면
    # 문자열 v에 대해 1단계부터 다시 수행
    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    # -> change_to_correct_parenthesis 다시 수행
    if is_correct_parenthesis(u):
        return u + change_to_correct_parenthesis(v)

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행
    #  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    #  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    #  4-3. ')'를 다시 붙입니다.
    #  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을
    #  뒤집어서 뒤에 붙입니다.
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])


    #  4-5. 생성된 문자열을 반환



def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)


print(get_correct_parentheses(balanced_parentheses_string))
