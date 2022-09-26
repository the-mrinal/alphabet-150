# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        tempA = headA
        tempB = headB
        
        limit = 0
        while tempA != tempB and limit < 2:
            if tempA:
                tempA = tempA.next
            else:
                limit += 1
                tempA = headB
            
            if tempB:
                tempB = tempB.next
            else:
                tempB = headA
        
        return tempA if tempA == tempB else None
            