# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4
# Input: l1 = [], l2 = [0]
# Output: [0]

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        
        currNode = dummy = ListNode(0)  
        
        while l1 is not None and l2 is not None:
            if l1.val<= l2.val:
                currNode.next = l1
                l1 = l1.next
            else:
                currNode.next = l2
                l2 = l2.next
            currNode = currNode.next   
        if l1 is None:
            currNode.next = l2
        if l2 is None:
            currNode.next = l1
        return dummy.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
