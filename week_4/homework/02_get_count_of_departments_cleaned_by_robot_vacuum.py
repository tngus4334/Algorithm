# 1. 현재 위치를 청소한다.
# 2.bfs룰 구현 visited = [1,2,3]
# 0은 청소하지 않은장소, 1은 청소하지 못하는 장소
# 2는 청소한 장소

# 2. 현재 위치에서 현재방향을 기준으로 왼쪽방향부터 차례대로 타색을진행
# -> 방향
#     r   c
# 북 -1    0
# 동  0    1
# 남  1    0
# 서  0    -1
#       북  동 남 서
# dr = [-1, 0, 1, 0] 각각 방향이 나타내는 row의 변동수
# dc = [0, 1, 0, -1]  colums이 각각방향에 따라 어떻게 달라지는지
# a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면,
# 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행
# 북왼회전 -> 서 0 -> 3
# 동왼회전 -> 북 1 -> 0
# 남왼회전 -> 동 2 -> 1
# 서왼회전 -> 남 3 -> 2

# b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# -> 현재 본 방향에서 청소할 곳이 없다면 다시 왼쪽으로 회전하라

# c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는
# 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# -> 모든 방향이 청소되어있다면 뒤로 한칸 후진
# 북 뒤돌기 -> 남 0 -> 2
# 동 뒤돌기 -> 서 1 -> 3
# 남 뒤돌기 -> 북 2 -> 0
# 서 뒤돌기 -> 동 3 -> 1

# d. 네 방향 모두 청소가 이미 되어있거나 벽이면서
# 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.


current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 방향 전환
def get_d_index_when_rotate_to_left(d):  # 현재방향이 왼쪽으로 회전한다면 몇번째 방향인가
    return (d + 3) % 4


# 후진
def get_d_index_when_go_back(d):
    return (d + 2) % 4


# 결국 반환해 줘야하는건 청소한 총 칸의개수
def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    n = len(room_map)
    m = len(room_map[0])  # 첫번째칸의 칼럼
    count_of_departments_cleaned = 1  # 청소하는 칸의 개수 -> 맨처음 칸은 청소한것이므로 1
    room_map[r][c] = 2  # 청소하면 room_map을 2로 업데이트
    queue = list([[r, c, d]])  # 모든 칸을 탐색하므로 bfs, 큐안에는 r, c, d를 넣는다 -> 현재 위치와 방향을 모두 기록해놓고 어떻게 탐색할지에 대한고민을 해야 하기 때문

    # 큐가 비어지면 종료
    while queue:
        r, c, d = queue.pop(0)  # 큐에서 맨앞원소
        temp_d = d  # 현재방향

        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)  # 현재방향에서 한번 왼쪽으로 회전한 값
            new_r, new_c = r + dr[temp_d], c + dc[temp_d]  # 왼쪽에서 가는 방향이 어디인가 -> 왼쪽으로 갔을 때 한칸 이동한 값

            # a
            if 0 <= new_r < n and 0 <= new_c < m and room_map[new_r][
                new_c] == 0:  # new_r(이동할 row값),new_c(이동할 columns)이 범위안에 들어와야함, 청소하지 않은 칸이어야 들어갈 수 있음
                count_of_departments_cleaned += 1
                room_map[new_r][new_c] = 2  # 청소했다고 기록 (업데이트)
                queue.append([new_r, new_c, temp_d])  # 새로운 칸의 값을 추가 -> 이동한 칸에서 다시한번 탐색해야 하기 때문
                break

            # c
            elif i == 3:  # 갈 곳이 없었던 경우
                new_r, new_c = r + dr[get_d_index_when_go_back(d)], c + dc[
                    get_d_index_when_go_back(d)]  # 후진한 것의 변화량을 r과 c에 적용
                queue.append([new_r, new_c, temp_d])
                # d
                if room_map[new_r][new_c] == 1:  # 뒤가 벽인 경우
                    return count_of_departments_cleaned


print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
