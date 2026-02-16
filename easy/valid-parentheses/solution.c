/*
[Description]
Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
  Every close bracket has a corresponding open bracket of the same type.

 
Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 
Constraints:

  1 <= s.length <= 104
  s consists of parentheses only '()[]{}'.

[Metadata]
- Difficulty: Easy
- Topics: String, Stack
- Slug: valid-parentheses
*/

// [Solution]
#define MAX 1000000
bool isValid(char* s) {
    char stack[MAX];

    int top=-1;
    
    for (int i = 0; s[i] != '\0'; i++) 
        
    {
        char charAt = s[i];
        if(charAt=='('||charAt=='{'||charAt=='[')
        {
            if(top>=MAX-1)
            {
                return false;
            }
            stack[++top]=charAt;

        }
        if(charAt==')'||charAt=='}'||charAt==']')
        {
            if (top == -1) 
            {
                // Stack underflow condition
                return false;
            }
            char opentemp=stack[top--];
            if( opentemp=='(' && charAt!=')' ||
                opentemp=='{' && charAt!='}' ||
                opentemp=='[' && charAt!=']')
            {
                return false;
            }
            
        }
    }
    return top == -1;

}