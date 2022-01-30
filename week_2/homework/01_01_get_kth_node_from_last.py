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

    # 1. 노드를 두개 잡는다
    # 2. 한 노드를 다른 노드보다 k만큼 떨어지게 한다
    # 3. 그리고 계속 한칸씩 같이 이동한다
    # 4. 만약 더 빠른노드가 끝에 도달했다면 느린노드는 끝에서 k만큼 떨어진 노드가 되므로 바로 반환

    #           1 2 3 4 5 6 7  8... 끝
    #      시작:ㅁ<-   6   ->ㅁ
    #  1번이동:    ㅁ<-   6   ->ㅁ
    #  끝나면 :          ㅁ<-   6   ->ㅁ -> 앞에있는 노드가 끝에 도달했을때 뒤에있는 노드는 6만큼 뒤에서 떨어진 노드가된다.

    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next  # k만큼 앞으로 가게 만들기

        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)
