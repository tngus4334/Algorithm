class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    # head가 4라고하면 새로운값인 3이 맨 꼭대기인 head로 올라와야하고 3이 4를 가리키도록 해야한다.
    # [3] -> [4]
    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    # pop 기능 구현
    # head
    # [3] -> [4] 일 때 head값을 없애주고 head값을 교체해줘야함
    def pop(self):
        if self.is_empty():  # stack이 비었다면
            return "Stack is Empty"
        delete_head = self.head  # 맨앞 값 반환
        self.head = self.head.next  # 현재 head의 다음값
        return delete_head

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data

    # is_Empty 기능 구현
    def is_empty(self):
        return self.head is None  # head가 none인지 아닌지만 알면됨


stack = Stack()
stack.push(3) # 데이터 넣기
print(stack.peek()) # 3
stack.push(4)
print(stack.peek()) # 4

print(stack.pop().data) # 4를 빼면서 출력
print(stack.peek()) # 3

print(stack.is_empty()) # false
print(stack.pop().data) # 3빼기
print(stack.is_empty()) # True
