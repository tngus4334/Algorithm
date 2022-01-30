# 1. 시작 노드를 큐에 넣는다
# 2. 현재 큐의 노드를 빼서 visited에 추가
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 queue에 추가

graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):
    queue = [start_node] # 시작노드 넣기
    visited = []
    while queue: # 큐가 비지 않을 때 까지
        current_node = queue.pop(0) # 맨앞부터 뽑아야하기 때문에 0
        visited.append(current_node)
        for adjacent_node in adj_graph[current_node]: # 인접그래프에서 인접한 노드
            if adjacent_node not in visited: # 인접한 노드가 방문하지 않았으면
                queue.append(adjacent_node) # 큐에다 추가

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드
