class MaxHeap:
    def __init__(self):
        self.items = [None] # 초기값
# 1. 새노드를 맨 끝에 추가한다.
# 2. 지금 넣은 새노드를 부모와 비교한다. 만약 부모보다 크다면 교체한다.
# 3. 이 과정을 꼭대기까지 반복한다.
    def insert(self, value):
        self.items.append(value) # 새 값 넣기
        cur_index = len(self.items) - 1 # 새 노드의 인덱스

        while cur_index > 1:
            parent_index = cur_index // 2 # 부모인덱스
            if self.items[cur_index] > self.items[parent_index]: # 새 노드의 인덱스 > 부모인덱스
                self.items[cur_index], self.items[parent_index] = self.items[parent_index],  self.items[cur_index] # 변경
                cur_index = parent_index # 새 노드의 인덱스가 부모 인덱스가 된다.
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)
#      9
#     4 2
#    3