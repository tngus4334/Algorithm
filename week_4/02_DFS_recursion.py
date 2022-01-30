# 1. 시작 노드(루트 노드)인 1부터 탐색
# 2. 현재 방문한 노드를 visited_array 에 추가
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드에 방문

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
visited = []

# visited_array = [1]
def dfs_recursion(adjacent_graph, cur_node, visited_array):
    visited_array.append(cur_node) # 시작노드를 visited_array에 추가
    for adjacent_node in adjacent_graph[cur_node]: # 인접노드 가져오기
        if adjacent_node not in visited_array: # 현재 인접한 노드가 없다면
            dfs_recursion(adjacent_graph, adjacent_node, visited_array) # 다시 함수호출

    return


dfs_recursion(graph, 1, visited)  # 1 이 시작노드
print(visited)
