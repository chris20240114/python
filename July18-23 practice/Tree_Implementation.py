from gettext import find
from os import remove
from re import X


class TreeNodes(object):
    def __init__(self, val):
        self.val = val
        self.children= []
        self.parent = None
    
    def find(self, value):
        if self.val == value:
            return self
        else:
            for i in self.children:
                return i.find(value)

    def insertNode(self, node1, val):
        node = self.find(node1)
        newNode=TreeNodes(val)
        newNode.parent = node
        node.children.append(newNode)
        
    def deleteNode(self, value):
        node=self.find(value)
        parent=node.parent
        for i in range(len(parent.children)):
            if parent.children[i].val == value:
                (parent.children.remove(parent.children[i]))
                return 1

tree = TreeNodes('R')
print(tree.val)

tree.insertNode('R', 'I')
print(tree.children)

tree.deleteNode('I')
print(tree.children)


#The delete and add node functions are not working.
