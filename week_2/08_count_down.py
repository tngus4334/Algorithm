def count_down(number):
    if number < 0:
        return
    print(number)  # number를 출력하고
    count_down(number - 1)  # count_down 함수를 number - 1 인자를 주고 다시 호출한다! 끝도없이 반복해서 에러남


# 재귀함수를 쓸 때는 탈출조건을 고민해야함
count_down(60)
