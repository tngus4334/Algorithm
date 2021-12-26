# [3] - > [4]
# 노드안에는 데이터와 다음칸을 나타내는 next라는 데이터가 있어야함
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node= Node(3)
first_node = Node(4)
node.next = first_node
# node [3] 3을 원래 가리키고 있는게 node
# node.next [4] #node에 next하니까 4
# node.next.data 4
print(node.next.data)
print(node.data)

class LinkedList:
    def __init__(self, data):
        self.head = Node(data) # 해당 data를 갖고있는 노드를 생성해서 넣어줌 -> head 노드로써 배달됨

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        cur = self.head
        print("cur is ", cur.data)
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
        # head에는 next가 없음 while문이 돌지않고 cur.next에 node(next)를 담아서
        # 링크드리스트의 원소가 추가가됨, 이상태에서 append(5)를 하면 cur= self.head 즉 3이라는 노드가됨
        #여기서는 next가 None이 아님 따라서 while문을 돌면서 cur이 다음노드인 4로 이동
        # [3] -> [4]

    # head node부터 시작으로 맨 뒤의 노드가 None일때까지 작업반복해줘야함
# [3] -> [4] -> [5] -> [6] -> None 으로 붙이고 싶으면
# append 함수를 실행하면 뒤에 data가 노드로 생성이됨
    #linked_list = LinkedList(3)  # 링크드리스트 정의
    #print(linked_list.head.next)

    def print_all(self): # head node로 시작해서 모든노드가 이어져있는구조 이값들을 일일히 출력
        print("hihihi")
        cur = self.head
        while cur is not None: #cur이 None이 아닐때까지
            print(cur.data) #계속해서 옮기면서 값출력
            cur = cur.next
# [3] -> [4] -> [5] -> [6] -> None

linked_list = LinkedList(3)

linked_list.append(4)
linked_list.append(5)
linked_list.print_all()