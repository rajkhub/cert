# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root,cnt = 0):
        if root == None:
            return cnt
        cnt +=1
        lft = self.maxDepth(root.left,cnt)
        rght = self.maxDepth(root.right,cnt)
        return max(lft,rght)

        
        
class Solution(object):
    def maxDepth(self, root ):
        if root == None:
            return 0
        else:
            lft = self.maxDepth(root.left)
            rght = self.maxDepth(root.right)
            return max(lft,rght) + 1 
 
 
 def maxDepth(self, root):
     if not root:
         return 0
     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
