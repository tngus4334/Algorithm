top_heights = [6, 9, 5, 7, 4]

# [0, 0, 2, 2, 4]
#  <- <- <- <- <-
#  6  9  5  7  4  4는 3번째 인덱스인 7을 배열에 저장하면된다. 그러나 순서로 반환해주고 있기 때문에 4를 넣어줘야함
# [0, 0, 0, 0, 4] 4번째 위치인 7이 레이저를 받음

#  <- <- <- <-
#  6  9  5  7
# [0, 0, 0, 2, 4] 2번째위치인 9가 레이저를 받음

#  <- <- <-
#  6  9  5
# [0, 0, 2, 2, 4] 2번째위치인 9가 레이저를 받음

#  <- <-
#  6  9
# [0, 0, 2, 2, 4] 레이저가 걸리지 않음

#  <-
#  6
# [0, 0, 2, 2, 4]

def get_receiver_top_orders(heights):
    answer = [0] * len(heights) # 0으로 초기화 시킨 배열
    while heights:
        height = heights.pop() # 맨 뒤에 있는 애들 하나씩 뽑음
        # [6, 9, 5, 7]
        for idx in range(len(heights) - 1, 0, -1): # 인덱스의 길이부터 시작해야 하기 때문에 -1함
            if heights[idx] > height: # 레이저가 박히는 순간
                # len(heights) : 스택에서 하나를 뺀 다음에 그 하나의 인덱스를 알기 위해서는 현재 나와있는 스택의 길이가 인덱스다
                answer[len(heights)] = idx + 1 # idex + 1 : 인덱스가 아니라 위치를 알려줘야 하기 때문
                break
    return answer


print(get_receiver_top_orders(top_heights))