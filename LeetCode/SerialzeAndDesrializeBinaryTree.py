# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def serial(root,string):
            if root == None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string  = serial(root.left,string)
                string  = serial(root.right,string)
            return string
        return serial(root,'')
        
        

    def deserialize(self, data):
        def deserial(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            
            root = TreeNode(l[0])
            l.pop(0)
            root.left = deserial(l)
            root.right = deserial(l)
            return root
        
        data_l = data.split(',')
        root = deserial(data_l)
        return root
        
