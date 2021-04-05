# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4]
# Output: Intersected at '2'

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        while headA != None:
            pB =headB
            while pB != None:
                if headA == pB:
                    return headA
                pB = pB.next
            headA = headA.next
        return None
 

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        pA = headA
        pB = headB
        
        while pA != pB:
            if pA is None:
                pA = headB
            else:
                pA = pA.next
            if pB is None:
                pB = headA
            else:
                pB = pB.next
        return pB
