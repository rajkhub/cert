# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        marker1 = head
        marker2 = head
        
        while marker2 != None and marker2.next != None:
            marker1 = marker1.next
            marker2 = marker2.next.next
            
            if marker1 == marker2:
                return True
        return False
    



class Node(object):
    def __init__(self,val):
        self.val = val
        self.nextnode = None
        
#Linked List Cycle Check

def cycle_Check(node):
    marker1 = node
    marker2 = node
    
    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        
        if marker2 == marker1:
            return True
    return False
    
a.nextnode = b
b.nextnode = c
c.nextnode = a
cycle_Check(a)
