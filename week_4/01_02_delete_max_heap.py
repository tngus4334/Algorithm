class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    # 1. 루트노드와 맨 끝에 있는 원소를 교체한다.
    # 2. 맨 뒤에 있는 원소를(원래 루트노드)를 삭제한다. 끝에 반환해줘야 하니까 저장해두자
    # 3. 변경된 노드와 자식 노드들을 비교한다. 두 자식 중 더 큰 자식과 비교해서 자신보다 자식이 더 크다면 자리를 바꿔주자
    # 4. 자식노드 둘보다 부모노드가 더 크거나 가장 바닥에 도달하지 않을때까지 3을 반복한다.
    # 5. 2 에서 제거한 원래 루트노드를 반환한다.
    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1] # 루트노드와 맨끝 노드를 변경
        prev_max = self.items.pop() # 해당배열에서 원소 뽑아서 변소에 담는다 -> 마지막에 반환

        cur_index = 1 # 꼭대기에 있는 루트노드의 위치

        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2 # 왼쪽자식
            right_child_index = cur_index * 2 + 1 # 오른쪽자식
            max_index = cur_index

            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]: # 왼쪽자식이 있고 왼쪽자식이 현재 탐색하고 있는 노드의 인덱스의 값보다 큰 경우
                max_index = left_child_index

            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]: # 오른쪽자식 존재, 오른쪽자식이 현재 max_index의 값보다 크다
                max_index = right_child_index

            if max_index == cur_index: # 현재있는 노드가 자식들보다 크다 -> 교체불필요
                break

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index] # max_index와 cur_index변경
            cur_index = max_index # cur_index는 max_index로 교체됨

        return prev_max


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)
print(max_heap.delete())
print(max_heap.items)
