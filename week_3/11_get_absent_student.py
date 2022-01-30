all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]

# 딕셔너리에 all_students를 넣고 present_students를 돌면서 키가 존재하는지 여부에 따라서 키를 제거하고
# 마지막까지 남아있는 키는 출석하지 않은 학생
def get_absent_student(all_array, present_array):
    student_dict = {}
    for key in all_array:
        student_dict[key] = True  # 아무 값이나 넣어도 상관 없다! 여기서는 키가 중요한거니까

    for key in present_array:  # dict에서 key 를 하나씩 없앤다
        del student_dict[key]

    for key in student_dict.keys():  # key 중에 하나를 바로 반환 한 명 밖에 없으니 이렇게 해도 된다.
        return key
    return


print(get_absent_student(all_students, present_students))