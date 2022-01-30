# 1. 시작노드를 스택에 넣는다
# 2. 현재 스택의 노드를 빼서 visited에 추가
# 3. 현재 방문한 노드와 인접한 노드 중에서 방문하지 않은 노드를 스택에 추가

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node] # stack을 시작하는 노드
    visited = [] # 방문한 노드 저장

    while stack: # stack이 비지 않을때까지
        current_node = stack.pop() # 현재 스택 빼기
        visited.append(current_node)  # [1]
        for adjacent_node in adjacent_graph[current_node]: # 인접한 노드 다 꺼내기
            if adjacent_node not in visited: # 이 노드가 visited에 없다면 방문하지 않은것이기 때문에
                stack.append(adjacent_node) # stack에 추가

    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드
