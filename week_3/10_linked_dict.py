class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):  # key에 따라 값이 달라짐
        for k, v in self.items:
            if k == key:
                return v


class LinkedDict:
    def __init__(self):
        self.items = [] # [LinkedTuple(),LinkedTuple(),,,,LinkedTuple()]
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value): # key에 대한 items를 찾아서 value 값을 추가
        index = hash(key) % len(self.items)
        self.items[index].add(key, value)

    # 만약, 입력된 key가 "fast" 인데 index 값이 2가 나왔다.
    # 현재 self.items[2] 가 [("slow", "느린")] 이었다!
    # 그렇다면 새로 넣는 key, value 값을 뒤에 붙여주자!
    # self.items[2] == [("slow", "느린") -> ("fast", "빠른")] 이렇게

    def get(self, key): # key를 주면 해당하는 값을 반환
        index = hash(key) % len(self.items)
        return self.items[index].get(key)

    # 만약, 입력된 key가 "fast" 인데 index 값이 2가 나왔다.
    # 현재 self.items[2] 가 [("slow", "느린") -> ("fast", "빠른")] 이었다!
    # 그렇다면 그 리스트를 돌면서 key 가 일치하는 튜플을 찾아준다.
    # ("fast", "빠른") 이 일치하므로 "빠른" 이란 값을 돌려주자!
