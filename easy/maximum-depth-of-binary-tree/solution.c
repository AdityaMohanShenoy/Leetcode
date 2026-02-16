/*
[Description]
Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

 
Constraints:

  The number of nodes in the tree is in the range [0, 104].
  -100 <= Node.val <= 100

[Metadata]
- Difficulty: Easy
- Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- Slug: maximum-depth-of-binary-tree
*/

// [Solution]
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int maxDepth(struct TreeNode* root) {
    // Base case: if the tree is empty
    if (root == NULL) {
        return 0;
    }

    // Recursively calculate the depth of the left and right subtrees
    int leftDepth = maxDepth(root->left);
    int rightDepth = maxDepth(root->right);

    // The maximum depth is the greater of the two depths, plus 1 for the current node
    return (leftDepth > rightDepth ? leftDepth : rightDepth) + 1;
}
