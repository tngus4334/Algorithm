import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


# 여러개중에서 M개를 고른 뒤 모든 치킨거리의 합이 가장 작게 되는 경우를 반환
# -> 여러개중에서 특정 개수를 뽑는 경우의 수
# -> 모든 경우의 수를 다 구해야함
# => 조합 !!!!


def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = [] # 치킨집위치 저장
    home_location_list = [] # 집위치 저장
    for i in range(n): # n : city_map의 행과 열의 길이
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i, j])

    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    # print(chicken_location_m_combinations) # 치킨집 조합
    # 최소도시치킨거리
    min_distance_of_m_combinations = sys.maxsize

    for chicken_location_m_combination in chicken_location_m_combinations:
        city_chicken_distance = 0 # 현재도시의 치킨거리 -> 0인 이유는 도시치킨거리는 각 집들의 치킨거리의 합이기 때문
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize
            for chicken_location in chicken_location_m_combination:
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )

            city_chicken_distance += min_home_chicken_distance # 도시의 최소 치킨거리에 집의 최소치킨거리를 더하면 된다
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, city_chicken_distance)

    return min_distance_of_m_combinations


print(get_min_city_chicken_distance(n, m, city_map))
