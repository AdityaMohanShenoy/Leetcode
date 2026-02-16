/*
[Description]
Insert Greatest Common Divisors in Linked List
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 
Example 1:

Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.

Example 2:

Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.

 
Constraints:

  The number of nodes in the list is in the range [1, 5000].
  1 <= Node.val <= 1000

[Metadata]
- Difficulty: Medium
- Topics: Linked List, Math, Number Theory
- Slug: insert-greatest-common-divisors-in-linked-list
*/

// [Solution]
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* insertGreatestCommonDivisors(struct ListNode* head){
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}
    if (head == NULL || head->next == NULL) {
        return head; // If the list is empty or has only one node, nothing to insert
    }
    struct ListNode *temp=head;
    while(temp != NULL && temp->next != NULL)
    {
    int a = temp->val;
    int b = temp->next->val;
    int res = gcd(a,b);
    struct ListNode *newnode=(struct ListNode *)malloc(sizeof(struct ListNode ));
    newnode->val=res;
    newnode->next=temp->next;
    temp->next=newnode;
    temp=temp->next->next;
    }
    return head;

}