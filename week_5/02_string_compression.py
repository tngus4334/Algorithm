# 모든 경우의 수를 파악
# 1에서 n의 길이로 자를 수 있다
# 1부터 n//2까지 자를 수 있음


input = "abcabcabcabcdededededede"


def string_compression(string):
    n = len(string)
    compression_length_array = [] # 가장 최소인 길이들을 모아놓는 변수
    for split_size in range(1, n//2 + 1):

        # 배열로 만들기
        splited = [string[i:i + split_size] for i in range(0, n, split_size)] # 0부터 n까지 인덱스를 split_size만큼 추가
        # print(splited)
        compressed = "" # 압축해서 표현한 문자
        count = 1 # 몇번이 반복되었는가 -> 이전값과 자기값을 비교하는것, 이미 나는 나와있어서 1
        for j in range(1, len(splited)): # 1부터 시작 -> 이전값이랑 지금값이랑 비교를 하기 위해서
            prev, cur = splited[j - 1], splited[j]
            if prev == cur:
                count += 1
            else:
                if count > 1:
                    compressed += (str(count) + prev)
                else:
                    compressed += prev
                count = 1
        if count > 1:
            compressed += (str(count) + splited[-1])
        else:
            compressed += splited[-1]
        # print(compressed)
        compression_length_array.append(len(compressed))
    return min(compression_length_array)


print(string_compression(input))