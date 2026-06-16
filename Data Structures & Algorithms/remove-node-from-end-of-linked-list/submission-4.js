/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} n
     * @return {ListNode}
     */
    removeNthFromEnd(head, n) {

        let length = 0
        let current = head

        while (current){
            length += 1
            current = current.next
        }
        if (n == length){
            return head.next
        }
        current = head;
        for (let i = 0; i < length - n - 1; i++){
            current = current.next
        }
        current.next = current.next.next

        return head
    }
}
