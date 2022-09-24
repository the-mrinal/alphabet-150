# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def divide(headLL):
            slow = headLL
            fast = headLL

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            temp = slow.next
            slow.next = None
            return [headLL,temp]

        def reverseLL(root):
            curr = root
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        def mergeLL(headA,headB):
            new_head = ListNode(None)
            curr = new_head

            while headA and headB:
                first = headA
                sec = headB
                headA = headA.next
                headB = headB.next

                first.next = sec
                sec.next = None

                curr.next = first
                curr = curr.next.next
            
            curr.next = headA or headB

            return new_head.next

        one,two = divide(head)

        two = reverseLL(two)

        return mergeLL(one,two)
