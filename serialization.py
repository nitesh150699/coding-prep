'''
Serialization : preorder with , seperated 
deserialization : pop top elem and preorder with forming tree
'''

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                return "None,"
            return str(node.value) + "," + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

    def deserialize(self, data):
        def dfs(data_list):
            if data_list[0] == "None":
                data_list.pop(0)  # Remove 'None'
                return None
            
            root = TreeNode(int(data_list[0]))
            data_list.pop(0)  # Remove the value from the list
            root.left = dfs(data_list)
            root.right = dfs(data_list)
            return root
        
        data_list = data.split(",")
        return dfs(data_list[:-1])  # Remove the last empty element due to trailing comma

