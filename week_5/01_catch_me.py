# 코니의 위치변화
# 코니는 처음 위치에서 1초 후 1만큼, 매초마다 이전 이동거리 +1만큼 움직임
# 즉 증가하는 속도가 1초마다 1씩 증가함
# 속도
# 1 2 3 4  5  6  7  8  9
# 위치 (처음 위치가 3이면) -> 시간에 따라 더해주면된다
#  1 2 3 4 5
# 3 4 6 9 13 18

# 브라운의 위치변화
# B-1, B+1, 2*B
# 2
# 1-1. 1
# 1-2. 3
# 1-3. 4
# 1-1-1. 0
# 1-1-2. 2
# 1-1-3. 2
# 1-2-1. 2
# 1-2-2. 4
# 1-2-3. 6
# 무수한 갈래로 선택지가 나눠지게 된다 -> 모든 경우의 수를 다 나열 -> BFC
# 잡았다! -> 같은 시간에 같은 위치에 존재
# 시간은 1씩 증가, 위치는 코니도 브라운도 값이 자유자재로 바뀐다
# 규칙적 -> 배열, 자유자재 -> 딕셔너리
# 각 시간마다 브라운이 갈 수 있는 위치를 저장하고 싶다 -> 이 정보가 있어야지만 이시간에 코니와 만날수있는지 없는지 알 수 있기 때문
# 브라운과 코니의 위치 구하기

from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0 # 현재시간
    queue = deque() # 브라운의 모든 경우의 수를 구하기 위한 큐만들기
    queue.append((brown_loc,0)) # 브라운의 위치 초기값과 시간 -> 위치와 시간 동시에 담음 -> 위치와 시간이 동시에 일치해야 만났다고 할 수 있기 때문
    visited = [{} for _ in range(200001)] # 브라운의 위치는 언제든지 변하기 때문에 저장 -> visited의 각 원소들은 각 시간 0초에 어느곳을 갔는지를 저장하기 위한 시간
    # visited[위치][시간]
    # visited[3]에 5라는 키가 있나? -> 3위치에 5초에 간적이있나?
    # 0    1   2     -> visited[2] = {0:True}
    # 2 -> 1   0     -> visited[1] = {1:True}
    #      3   2     -> visited[3] = {1:True}
    #      4   3     -> visited[4] = {1:True}
    #          4
    #          8

#     visited[0] = {    # 0번째 원소에 0번째 시간에 갔던 곳을 저장
#         2 : True # 키값 설정 -> 다른거 넣어도됨
#     }
#     visited[1] = {
#         1 : True
#         3 : True
#         4 : True
#     }
#     visited[1] = {
#         0 : True
#         2 : True
#         4 : True
#         3 : True
#         8: True
#     }
# -> 이렇게 시간과 위치를 알고있으면 즉각적으로 알 수 있는 자료구조가 됨

    while cony_loc <= 200000: # 코니가 범위를 벗어나면 게임이 끝난다
        cony_loc += time # 코니의 위치에 시간더한다 -> 시간만큼 +1 +2 +3 ...
        if time in visited[cony_loc]:
            return time # 이 시간대에 방문하게 된 것이므로 코니와 브라운이 만나게 된 시점을 알 수 있다

        for i in range(0, len(queue)): # 큐의 길이만큼 반복
            current_position, current_time = queue.popleft() # 현재위치와 현재시간


            new_position = current_position - 1
            new_time = current_time + 1  # 새로운 시간

            if 0 < new_position <= 200000:
                queue.append((new_position,new_time)) # 각각의 포지션에 대해서 큐에다가 추가 -> (3번 반복)모든 경우의 수를 다 구하기 위해 각각의 갈래길들을 다 만들어줌

            new_position = current_position + 1
            if 0 < new_position <= 200000:
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 < new_position <= 200000:
                queue.append((new_position, new_time))

        time += 1

    return -1 # while문이 끝났을 때도 없다면


print(catch_me(c, b))