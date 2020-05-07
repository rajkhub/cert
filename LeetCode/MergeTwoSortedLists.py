# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4

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
