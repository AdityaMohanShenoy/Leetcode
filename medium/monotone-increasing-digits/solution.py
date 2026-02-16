"""
[Description]
Monotone Increasing Digits
https://leetcode.com/problems/monotone-increasing-digits/

An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

 
Example 1:

Input: n = 10
Output: 9

Example 2:

Input: n = 1234
Output: 1234

Example 3:

Input: n = 332
Output: 299

 
Constraints:

  0 <= n <= 109

[Metadata]
- Difficulty: Medium
- Topics: Math, Greedy
- Slug: monotone-increasing-digits
"""

// [Solution]
class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(str(n))  # editable digits
        i = 0

        # 1) Find first index where monotonicity breaks: s[i] > s[i+1]
        while i < len(s) - 1 and s[i] <= s[i + 1]:
            i += 1

        # Already monotone
        if i == len(s) - 1:
            return n

        # 2) Decrease s[i] and propagate left if needed
        s[i] = str(int(s[i]) - 1)
        # Move left while the left neighbor is now greater than current
        while i > 0 and s[i] < s[i - 1]:
            s[i - 1] = str(int(s[i - 1]) - 1)
            i -= 1

        # 3) Fill everything to the right of index i with '9'
        j = i + 1
        while j < len(s):
            s[j] = '9'
            j += 1

        return int("".join(s))
