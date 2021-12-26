input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        # index 0 -> 3
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

        #print(max_alphabet_index)
        return chr(max_alphabet_index + ord("a"))
        # a->0
        # a -> ord(a) -> 97 - ord(a) = 0
        # 0 -> a
        # 0 -> 0+ord(a) -> 97 -> chr(97) -> a


result = find_max_occurred_alphabet(input)
print(result)