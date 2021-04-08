# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack=[root]
        parent={root:None}
        
        while stack:
            popped = stack.pop()
            if popped.left != None:
                parent[popped.left] =popped
                stack.append(popped.left)
            if popped.right != None:
                parent[popped.right] = popped
                stack.append(popped.right)
        
        ancestors=set()
        
        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]
        return q
