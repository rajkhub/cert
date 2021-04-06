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
        
#         while p not in parent or q not in parent:
        while len(stack)!=0:
            node=stack.pop()
            
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors= set()
        
#The Below Logic will save all possible ancestors in Ancestors Set
        while p:
            ancestors.add(p)
            p = parent[p]
# If there is any matching common Parent in ancestors Set, it will retrieve lowest common Ancestor
        while q not in ancestors:
            q= parent[q]
        return q
