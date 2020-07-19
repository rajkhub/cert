#Binary Tree Implementation

class BinaryTree(object):
    
    def __init__(self,root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newnode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self,newnode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getLeft(self):
        return self.leftChild
    
    def getRight(self):
        return self.rightChild
    
    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key



r = BinaryTree('a')
print r.getRootVal()
print r.getLeft()
r.insertLeft('b')
print r.getLeft().getRootVal()
r.insertRight('c')
print r.getRight().getRootVal()
