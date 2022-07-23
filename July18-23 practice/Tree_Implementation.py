from gettext import find
from os import remove
from re import X


class TreeNodes(object):
    def __init__(self, val, child):
        self.val = val
        self.children= [child]
        self.parent = None
    
def insertNode(self, node1, val):
        node = self.find(node1)
        newNode=tree(val, node)
        node.children.append(newNode)
        pass
        '''if self.val:
            if val < self.val:
                    if self.left is None:
                        self.left = Tree(val)
                    else:
                        self.left.insert(val)
            elif val > self.val:
                    if self.right is None:
                        self.right = Tree(val)
                    else:
                        self.right.insert(val)
        else:
            self.val = val'''

tree = TreeNodes('R', [1, 2, 3, 4, 5])
print(tree.val)
tree.parent = 'R' 
print(tree.children)

insertNode('R', 'U')

def deleteNode(self, value):
    node=self.find(value)
    parent=node.parent
    for i in range(len(parent.children)):
        if parent.chidlren[i].value == value:
            remove(parent.children[i])
            return 1
deleteNode('R')

#The delete and add node functions are not working.
