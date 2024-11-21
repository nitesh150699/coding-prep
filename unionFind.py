n = 5  
parent = list(range(n))
rank = [0] * n

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    
    if rootX != rootY:
        # Union by rank
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
