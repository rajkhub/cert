#Trim a Binary Search Tree between two numbers

def TrimBinary(tree,Min,Max):
    
    tree.left = TrimBinary(tree.left,Min,Max)
    tree.right = TrimBinary(tree.right,Min,Max)
    
    if Min <= tree <= Max:
        return tree
    if Min < tree:
        return tree.left
    if Max <= tree:
        return tree.right
        
