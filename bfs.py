
# in bfs ..if value enters dq it will be marked as vis
from collections import deque

def bfs(start_node, graph):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    
    res = []
    
    while queue:
        node = queue.popleft()
        res.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return res

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1, 5],
    5: [4]
}

result = bfs(0, graph)
print("BFS Traversal Result:", result)
