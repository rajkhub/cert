#Input: 1->1->2
#Output: 1->2

def deleteDuplicates(self, head):
    curr = head
    while curr is not None and curr.nex is not None t:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
