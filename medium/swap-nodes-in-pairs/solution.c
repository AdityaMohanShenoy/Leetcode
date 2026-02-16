/*
[Description]
Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 
Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:

Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 
Constraints:

  The number of nodes in the list is in the range [0, 100].
  0 <= Node.val <= 100

[Metadata]
- Difficulty: Medium
- Topics: Linked List, Recursion
- Slug: swap-nodes-in-pairs
*/

// [Solution]
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head)
{
    struct ListNode *temp = (struct ListNode *)malloc(sizeof(struct ListNode));
    temp->val = 0;
    temp->next = head;
    
    struct ListNode *prev = temp;
    struct ListNode *current = head;

    while (current != NULL && current->next != NULL)
    {
        struct ListNode *second = current->next;
        struct ListNode *next_pair = second->next;
        
        // Swapping nodes
        second->next = current;
        current->next = next_pair;
        prev->next = second;

        // Move to the next pair
        prev = current;
        current = next_pair;
    }

    head = temp->next;
    free(temp); // Freeing the temporary node
    return head;
}
