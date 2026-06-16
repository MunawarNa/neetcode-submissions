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
     * @return {void}
     */
    reorderList(head) {

        if (head === null || head.next === null) {
            return head;
        }

        let slow = head;
        let fast = head;

        while (fast && fast.next){
            slow = slow.next;
            fast = fast.next.next;
        }

        let prev = null;
        let current = slow;

        while(current){
            let next_ = current.next;
            current.next = prev;
            prev = current;
            current = next_;
        }

        let first = head ;
        let second = prev;

        while (second.next){
            let tmp1 = first.next;
            let tmp2 = second.next;

            first.next = second;
            first = tmp1;

            second.next = first
            second = tmp2;
        }
        return head
    }
    
}
