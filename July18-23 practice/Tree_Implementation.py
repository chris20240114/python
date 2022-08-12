from gettext import find
from os import remove
from re import X


class TreeNodes(object):
    def __init__(self, val):
        self.val = val
        self.children= []
        self.parent = None
    
    def BFS(self, value):
        if self.val == value:
            print(type(self))
            return self
        else:
            for i in self.children:
                return i.BFS(value)

    def DFS(self, value):
        Visited = []
        if self.val == value:
            print(Visited)
            return self
        elif len(self.children) == 0:
            Visited.append(self.val)
            return self.parent.DFS(value)
        elif len(self.children) != 0:
            for i in self.children:
                if i.val not in Visited:
                    return i.DFS(value)
            return self.parent.DFS(value)




    def insertNode(self, node1, val):
        node = self.BFS(node1)
        newNode=TreeNodes(val)
        newNode.parent = node
        node.children.append(newNode)
        
    def deleteNode(self, value):
        node=self.BFS(value)
        parent=node.parent
        for i in range(len(parent.children)):
            if parent.children[i].val == value:
                (parent.children.remove(parent.children[i]))
                return 1

tree = TreeNodes('A')
tree.insertNode('A', 'B')
tree.insertNode('A', 'C')
tree.insertNode('B', 'D')
tree.insertNode('B', 'E')
print(tree.BFS('C').val)
print(tree.children)


#The delete and add node functions are not working.
