# [1,2,3,4,5,6,7,8,9]
# 좌석 [1,2] 2
# [1,2] [2,1]
# 좌석 [1,2,3] 3
# [1,2,3] [2,1,3] [1,3,2]
# 좌석 [1,2,3,4] 5
# [1,2,3,4] [1,2,4,3] [1,3,2,4] [2,1,3,4] [2,1,4,3]
# 좌석 [1,2,3,4,5] 8
# [1,2,3,4,5] [1,2,3,5,4] [2,1,3,4,5] [2,1,3,5,4]
# [1,2,4,3,5] [2,1,4,3,5] [2,1,3,4,5] [1,3,2,4,5]
# -> 피보나치 수열

# 좌석이 i개 있다.
# 1.                i번째 좌석에 i번 티켓을 가진 사람이 그대로 앉는 경우
# 1 2 3 4 5 6 ......i
# i-1 좌석들을 맘껏 배치할 수 있는 경우의 수

# 2. i번째 티켓을 가진 사람이 i-1번째 앉을 경우
#                    i i-1  # i가 i-1의 자리에 앉을 경우 i-1는 무조건 i자리에 앉아야한다
# 1 2 3 4 5 6 ......i-1 i
# i-2 번째 좌석들은 맘대로 배치할 수 있는 경우의 수

# F(N) = N명의 사람들을 좌석에 배치하는 방법
#      = N-1명의 사람들을 좌석에 배치하는 방법 + N-2명의 사람들을 좌석에 배치하는 방법
#      = F(N-1) + F(N-2)

# [1,2,3,4,5,6,7,8,9]
# 1,2,3 F(3) = 3
# 5,6   F(2) = 2
# 8,9   F(2) = 2
# 3 * 2 * 2 = 12

seat_count = 9
vip_seat_array = [4, 7]


memo = {
    1: 1,  # 이 문제에서는 Fibo(1) = 1, Fibo(2) = 2 로 시작
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1 # 모든 방법의 수 -> 아무자리도 안움직이면 1개, 곱연산 할것이기때문
    current_index = 0 # 맨처음 시작하게 되는 인덱스
    # [4 ,7]
    # [(1,2,3),4,(5,6),7,(8,9)]
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1 # 인덱스를 번호로 만들어야하기 때문
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo) # current_index를 fixed_seat_index에서 빼면 사이에 있는 좌석의 개수가 나옴
        all_ways *= count_of_ways # 곱연산
        current_index = fixed_seat_index + 1 # 이미 1,2,3을 해줬기 때문에 4 다음인덱스를 보라고 다음 칸으로 넘겨줌
    # [(8,9)]처럼 뒤에 남아있는 애들을 위해서
    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo) # 총개수에서 9-7
    all_ways *= count_of_ways
    return all_ways


print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
