/*
[Description]
Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 
Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

 
Constraints:

  The number of nodes in the list is sz.
  1 <= sz <= 30
  0 <= Node.val <= 100
  1 <= n <= sz

 
Follow up: Could you do this in one pass?

[Metadata]
- Difficulty: Medium
- Topics: Linked List, Two Pointers
- Slug: remove-nth-node-from-end-of-list
*/

// [Solution]
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // Create a dummy node before head
    struct ListNode* dummy = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = head;

    struct ListNode* fast = dummy;
    struct ListNode* slow = dummy;

    // Move fast pointer n+1 steps ahead so slow ends up just before target
    for (int i = 0; i <= n; i++) {
        fast = fast->next;
    }

    // Move both until fast reaches the end
    while (fast != NULL) {
        fast = fast->next;
        slow = slow->next;
    }

    // slow->next is the node to delete
    struct ListNode* toDelete = slow->next;
    slow->next = slow->next->next;
    free(toDelete);

    // New head may have changed if we deleted the first node
    struct ListNode* newHead = dummy->next;
    free(dummy);

    return newHead;
}
