from collections import defaultdict

def find_bridges(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * n 
    low = [-1] * n   
    bridges = []     
    time = [0]      

    def dfs(u, parent):
        disc[u] = low[u] = time[0]
        time[0] += 1

        for v in graph[u]:
            if disc[v] == -1: 
                dfs(v, u)
                low[u] = min(low[u], low[v])  

                if low[v] > disc[u]:
                    bridges.append((u, v))

            elif v != parent:  
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)

    return bridges

if __name__ == "__main__":
    n = 5 
    edges = [
        (0, 1), (1, 2), (2, 0), (1, 3), (3, 4)
    ]
    print("Bridges in the graph:", find_bridges(n, edges))
