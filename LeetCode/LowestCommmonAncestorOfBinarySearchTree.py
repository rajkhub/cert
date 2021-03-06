Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

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

    
#Recursion   
    
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def recur(root, p, q):
            if root == None:
                return None
            if root == p or root ==q:
                return root
        
            left = recur(root.left,p,q) 
            right = recur(root.right,p,q)
        
            if left != None and right != None:
                return root
            if left == None and right == None:
                return None
            if left != None:
                return left
            if right != None:
                return right            
            
        return recur(root, p, q)    

