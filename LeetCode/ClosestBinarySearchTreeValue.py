# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root is None:
            return float('inf')

        if root.val == target:
            return root.val
        elif root.val < target:
            rightRes = self.closestValue(root.right, target)
            if abs(root.val - target) < abs(rightRes - target):
                return root.val
            else:
                return rightRes
        elif root.val > target:
            leftRes = self.closestValue(root.left, target)
            if abs(root.val - target) < abs(leftRes - target):
                return root.val 
            else:
                return leftRes

            
        
