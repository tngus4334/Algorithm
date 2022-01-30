# 속한 노래가 가장 많이 재생된 장르 -> 정렬
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록
# 3. 장르 내에서 재생횟수가 같다면 고유번호가 낮은 노래 먼저 수록
# 장르별로(key) 우선 재생된 횟수(value)를 저장해야 한다.
# 장르별로 곡의 정보(인덱스, 재생횟수)를 배열로 묶어 저장한다

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)  # 장르의 길이
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}  # 장르별로 인덱스와 플레이를 담은 배열을 딕셔너리 형태로 저장
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:  # 키가 없다면
            genre_total_play_dict[genre] = play  # 그대로 대입
            genre_index_play_array_dict[genre] = [[i, play]]  # 배열로 만든다 -> 장르별로 여러곡이 쌓인 것을 저장하기 위해
        else:  # 키가 존재하면
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])
    # print(genre_total_play_dict) -> 장르별 총 곡의 재생횟수
    # print(genre_index_play_array_dict) -> 장르별 곡의 인덱스와 재생횟수

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True) # genre_total_play_dict 정렬
    # print(sorted_genre_play_array)
    result = [] # 결과값
    for genre, _value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre] # [[1, 600], [4, 2500]]
        sorted_index_play_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)
        # print(sorted_index_play_array)
        for i in range(len(sorted_index_play_array)):
            if i > 1: # 장르별 2곡만
                break
            result.append(sorted_index_play_array[i][0])
    return result


print(get_melon_best_album(genres, plays))
