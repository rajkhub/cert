# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        current = head
        prev = None
        nxt = None
           
        while(current):
            nxt = current.next
            current.next = prev
            
            prev = current
            current = nxta
        
        return prev
            
        



#Linked List Reversal

def LinkListRev(head):
    current = head
    previous = None
    nextnode = None
#     1->2->3
    while current is not None:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode
    
    return previous
    


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print a.val
print a.nextnode.val
print b.nextnode.val
print c.nextnode.val

LinkListRev(a)
