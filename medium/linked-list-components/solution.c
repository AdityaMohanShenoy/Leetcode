/*
[Description]
Linked List Components
https://leetcode.com/problems/linked-list-components/

You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.

 
Example 1:

Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.

Example 2:

Input: head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

 
Constraints:

  The number of nodes in the linked list is n.
  1 <= n <= 104
  0 <= Node.val < n
  All the values Node.val are unique.
  1 <= nums.length <= n
  0 <= nums[i] < n
  All the values of nums are unique.

[Metadata]
- Difficulty: Medium
- Topics: Array, Hash Table, Linked List
- Slug: linked-list-components
*/

// [Solution]
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int numComponents(struct ListNode* head, int* nums, int numsSize) {
    int count = 0;
    int inComponent = 0;
    struct ListNode* curr = head;

    // Iterate through the linked list
    while (curr != NULL) {
        // Check if the current node's value is in nums
        int isInNums = 0;
        for (int i = 0; i < numsSize; i++) {
            if (nums[i] == curr->val) {
                isInNums = 1;
                break;
            }
        }

        // If the value is in nums and we're not currently in a component, start a new component
        if (isInNums) {
            if (!inComponent) {
                count++;
                inComponent = 1;
            }
        } else {
            // If the value is not in nums, we're no longer in a component
            inComponent = 0;
        }

        // Move to the next node
        curr = curr->next;
    }

    return count;
}

