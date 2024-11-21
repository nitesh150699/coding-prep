'''
- Used for range queries . ex : sum of range | max or min of range . it avoids re computing the results

Building
- segment tree len = 4*n | 
- provide indexes left = 2*i + 1 and right = 2*i +2 .. so seg[ind] = max( seg[left] , seg[right]) and base case filling leaf nodes

Querying
- if low , high completely lies in l , h we return seg[ind]
- if out of bound return 0
- else traverse left and right and return left + right

update:
try to find node to update and let function do its job

'''

def build(data):
    n = len(data)
    tree = [0] * (4 * n)  # Allocate space for the segment tree
    _build_recursive(data, tree, 0, 0, n - 1)
    return tree, n

####################################


def _build_recursive(data, tree, node, start, end):
    if start == end:
        tree[node] = data[start]
    else:
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        _build_recursive(data, tree, left_child, start, mid)
        _build_recursive(data, tree, right_child, mid + 1, end)
        tree[node] = tree[left_child] + tree[right_child]

#########################################
def update(tree, idx, value, node, start, end):
    if start == end:
        tree[node] = value
    else:
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        if start <= idx <= mid:
            update(tree, idx, value, left_child, start, mid)
        else:
            update(tree, idx, value, right_child, mid + 1, end)
        tree[node] = tree[left_child] + tree[right_child]


#############################################################
def query(tree, L, R, node, start, end):
    if R < start or end < L:
        return 0
    if L <= start and end <= R:
        return tree[node]
    
    mid = (start + end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2
    left_sum = query(tree, L, R, left_child, start, mid)
    right_sum = query(tree, L, R, right_child, mid + 1, end)
    
    return left_sum + right_sum

# Example usage
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]  # Initial array
    tree, n = build(data)

    # Query the sum of range [1, 4] which is 3 + 5 + 7 = 15
    print("Sum of range [1, 4]:", query(tree, 1, 4, 0, 0, n - 1))

    # Update index 2 with value 10
    update(tree, 2, 10, 0, 0, n - 1)

    # Query the sum of range [1, 4] again, now it should be 3 + 10 + 7 = 20
    print("Sum of range [1, 4] after update:", query(tree, 1, 4, 0, 0, n - 1))
