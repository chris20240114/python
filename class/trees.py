'''class TreeNode:
    def __init__(self, data): 
        self.data=data
        self.children= []
        self.parent = None
    
    def add_child(self, child):
        self.parent=child
        self.children.append(child)
'''

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

if __name__ == '__main__': 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node (7)

    







