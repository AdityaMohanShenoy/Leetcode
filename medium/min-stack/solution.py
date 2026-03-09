"""
[Description]
Min Stack
https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

  MinStack() initializes the stack object.
  void push(int val) pushes the element val onto the stack.
  void pop() removes the element on the top of the stack.
  int top() gets the top element of the stack.
  int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

 
Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

 
Constraints:

  -231 <= val <= 231 - 1
  Methods pop, top and getMin operations will always be called on non-empty stacks.
  At most 3 * 104 calls will be made to push, pop, top, and getMin.

[Metadata]
- Difficulty: Medium
- Topics: Stack, Design
- Slug: min-stack
"""

// [Solution]
class MinStack:

    def __init__(self):
        # The main stack stores our elements
        self.stack = []
        # The min_stack stores the minimum at each point
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        
        # If min_stack is empty, the current val is the min.
        # Otherwise, compare val with the top of min_stack.
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = self.min_stack[-1]
            self.min_stack.append(min(val, current_min))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]