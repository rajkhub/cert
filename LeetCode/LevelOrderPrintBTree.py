#Level Order Print if Binary Tree
class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

import collections
def levelOrderPrint(tree):
    nodes = collections.deque([tree])
#     nodes = [tree]
    currentCount =1
    nextcount = 0
    
    while len(nodes)!=0:
        currentnode = nodes.popleft()
#         currentnode = nodes.pop(0)       
        currentCount -=1
        print currentnode.val,
        
        if currentnode.left is not None:
            nodes.append(currentnode.left)
            nextcount +=1
        if currentnode.right is not None:
            nodes.append(currentnode.right)
            nextcount +=1
        
        if currentCount ==0:
            print '\n',
            currentCount,nextcount = nextcount,currentCount
        
    
    
root = Node(2)
root.left = Node(1)
root.right = Node(3)
root.left.right = Node(5)
root.right.right = Node(4)

printTree(root)
