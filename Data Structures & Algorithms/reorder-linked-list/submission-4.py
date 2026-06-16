# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head and not head.next:
            return head

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        prev = None
        curr =  slow
        while curr:
            next_ = curr.next
            curr.next = prev
            prev =  curr
            curr = next_

        first = head
        second = prev
        while second.next:
            temp1 = first.next
            first.next  = second
            first = temp1

            temp2 = second.next
            second.next = first
            second = temp2

        
        