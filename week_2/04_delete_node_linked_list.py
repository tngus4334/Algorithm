class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):  # 몇번째인지도 알아야하고 무슨값을 넣을지도 알아야함
        new_node = Node(value)  # [6] 생성
        if index == 0:
            new_node.next = self.head  # [6] -> [5] 이거 안넣으면 이전에 있던 head node들이 전부 사라짐
            self.head = new_node  # head -> [6] -> [5] -> ....
            return

        node = self.get_node(index - 1)  # 클래스내부 함수 호출 # [5]
        next_node = node.next  # [12]
        node.next = new_node  # [5] -> [6]
        new_node.next = next_node  # [6] -> [12]
        return

    def delete_node(self, index):
        if index == 0:  # head node 제거
            self.head = self.head.next
            return

        node = self.get_node(index - 1)
        node.next = node.next.next

        return


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)
print(linked_list.get_node(0).data)  # -> 5를 들고 있는 노드를 반환해야 합니다!
# print(linked_list.get_node(1).data) # 12
# [5] -> [6] -> [12] -> [8]

linked_list.add_node(1, 6)
linked_list.print_all()
linked_list.delete_node(0)
linked_list.print_all()
