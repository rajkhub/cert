# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6


class Solution:
    def mergeKLists(self, lists):
        head = ListNode(0)
        for i in range(len(lists)):
            ls = self.mergeTwoLists(head.next,lists[i])
            head.next = ls
        return head.next
        
        
    def mergeTwoLists(self,l1,l2):
        head = dummy = ListNode(0)
        
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next 
                
        if l1 is None:
            dummy.next = l2
        if l2 is None:
            dummy.next = l1
        
        return head.next
