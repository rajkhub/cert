#Binary Search Tree check

class Node(object):
    def __init__(self,k,val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None

def TreeMax(node):
    if not node:
        return float("-inf")    
    maxleft = TreeMax(node.left)
    maxright = TreeMax(node.right)
    return max(maxleft,maxright,node.key)

def TreeMin(node):
    if not node:
        return float("inf")
    minleft = TreeMin(node.left)
    minright = TreeMin(node.right)
    return min(minleft,minright,node.key)

def verify(node):
    if not node:
        return True
    if (TreeMax(node.left) <= node.key <= TreeMin(node.right) and verify(node.left) and verify(node.right)):
        return True
    else:
        return False
        
        
root= Node(10, "Hello")
root.left = Node(5, "Five")
root.right= Node(30, "Thirty")

print verify(root)
#True

root = Node(10, "Ten")
root.right = Node(20, "Twenty")
root.left = Node(5, "Five")
root.left.right = Node(15, "Fifteen")

print(verify(root))
#False
