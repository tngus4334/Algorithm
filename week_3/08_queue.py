class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    #     head   tail
    # 현재 [4] -> [2] 인 상태에서 new node를 만든다.
    # new_node = Node(value)

    # head   tail
    # [4] -> [2] -> [3]
    # self.tail.next = new_node

    # head          tail
    # [4] -> [2] -> [3] 인 상태로 만들면 된다.
    # self.tail = new_node
    def enqueue(self, value):
        new_node = Node(value)
        # self.head와 self.tail에 None을 넣은 상태로 시작한다 -> None이 head이자 tail
        if self.is_empty(): # 만약 비어있다면,
            self.head = new_node  # head 에 new_node를
            self.tail = new_node  # tail 에 new_node를 넣어준다.
            return
        self.tail.next = new_node
        self.tail = new_node

    # head          tail
    # [4] -> [2] -> [3]
    # head   tail
    # [2] -> [3]        [4]반환
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"  # 만약 비어있다면 에러

        delete_head = self.head  # 제거할 node를 저장
        self.head = self.head.next  # 그리고 head 를 현재 head 의 다음것으로 변경
        return delete_head.data  # 제거할 node 반환

    def peek(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.head.data # head 반환

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())

print(queue.dequeue()) # 3
print(queue.peek()) # 4
print(queue.is_empty())
print(queue.dequeue()) # 4
print(queue.dequeue()) # 5
print(queue.dequeue()) # 에러
