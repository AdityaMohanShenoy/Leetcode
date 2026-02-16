/*
[Description]
Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 
Constraints:

  The number of nodes in each linked list is in the range [1, 100].
  0 <= Node.val <= 9
  It is guaranteed that the list represents a number that does not have leading zeros.

[Metadata]
- Difficulty: Medium
- Topics: Linked List, Math, Recursion
- Slug: add-two-numbers
*/

// [Solution]
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdlib.h>

// Definition for singly-linked list.


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int carry = 0;

    // Dummy head to simplify handling
    struct ListNode *dummyHead = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummyHead->next = NULL;
    struct ListNode *current = dummyHead;

    // Traverse both lists and handle carry
    while (l1 != NULL || l2 != NULL || carry != 0) {
        int ele1 = (l1 != NULL) ? l1->val : 0; // Get l1 value or 0 if NULL
        int ele2 = (l2 != NULL) ? l2->val : 0; // Get l2 value or 0 if NULL
        
        int sum = ele1 + ele2 + carry;
        carry = sum / 10; // Calculate carry for next iteration

        // Create new node with the sum % 10 as the value
        struct ListNode *newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = sum % 10;
        newNode->next = NULL;

        current->next = newNode;  // Attach new node to the result
        current = newNode;        // Move to the next node

        // Move to the next nodes in l1 and l2 if they exist
        if (l1 != NULL) l1 = l1->next;
        if (l2 != NULL) l2 = l2->next;
    }

    // Return the head of the result list, skipping the dummy node
    return dummyHead->next;
}
