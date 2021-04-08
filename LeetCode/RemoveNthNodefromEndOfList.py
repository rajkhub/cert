# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Input: head = [1], n = 1
# Output: []

class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        
        for i in range(n):
            fast = fast.next
            
        if fast == None:
            return head.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return head
