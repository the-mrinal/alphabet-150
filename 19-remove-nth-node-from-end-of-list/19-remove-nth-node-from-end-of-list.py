# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = None
        
        fast = head
        
        count = 1
        
        while fast and fast.next:
            fast = fast.next
            if count >= n:
                if slow:
                    slow = slow.next
                else:
                    slow = head
            count += 1
            
        if not slow:
            return head.next
        
        slow.next = slow.next.next
        
        return head