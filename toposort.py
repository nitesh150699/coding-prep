from collections import deque, defaultdict

'''
conditions to remember:

indegree updation
len(topo_order) == num_nodes:

'''

def topological_sort_bfs(num_nodes, edges):
    in_degree = [0] * num_nodes
    adj_list = defaultdict(list)

    for u, v in edges:
        adj_list[u].append(v)
        in_degree[v] += 1

    queue = deque([node for node in range(num_nodes) if in_degree[node] == 0])
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == num_nodes:
        return topo_order
    else:
        return []  

num_nodes = 6
edges = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1)
]

topo_order = topological_sort_bfs(num_nodes, edges)
if topo_order:
    print(f"Topological Sort: {topo_order}")
else:
    print("The graph has a cycle, so no topological ordering exists.")
