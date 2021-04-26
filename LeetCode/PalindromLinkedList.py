# Input: head = [1,2,2,1]
# Output: true

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):

        curr = head
        stack =[]

        while curr != None:
            stack.append(curr.val)
            curr = curr.next

        while head != None:
            i = stack.pop()

            if head.val != i:
                return False
    
            head = head.next

        return True
