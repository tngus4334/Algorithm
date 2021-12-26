input = "abadabac"


def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26
    # abcd....z순으로 for문을 돌기 때문에 c와 d순서대로 꺼낼 수 밖에없음
    # 기존문자열의 순서를 보장해주지 않는다.
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = [] # 반복되지 않는것을 찾아야하기 때문에 하나만 나온거 찾아야함
    for index in range(len(alphabet_occurrence_array)): # 알파벳의 길이만큼 반복
        alphabet_occurrence = alphabet_occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a"))) # index를 알파벳으로 바꿔줘야함

    # print(not_repeating_character_array)
    for char in string:
        if char in not_repeating_character_array:
            return char


result = find_not_repeating_character(input)
print(result)