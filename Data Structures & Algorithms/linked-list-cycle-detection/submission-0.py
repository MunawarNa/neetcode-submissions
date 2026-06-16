# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = []
        
        curr = head

        while curr :
            if curr.val in visited_nodes:
                return True
            else:
                visited_nodes.append(curr.val)
                curr = curr.next
        return False

            
        