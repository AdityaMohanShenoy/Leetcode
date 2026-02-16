"""
[Description]
Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without duplicate characters.

 
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 
Constraints:

  0 <= s.length <= 5 * 104
  s consists of English letters, digits, symbols and spaces.

[Metadata]
- Difficulty: Medium
- Topics: Hash Table, String, Sliding Window
- Slug: longest-substring-without-repeating-characters
"""

// [Solution]
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = 0
        s1 = set()     # keep your s1 idea, but make it a set
        max1 = 0

        while r < len(s):   # was r <= len(s) (out of bounds)
            if s[r] not in s1:
                s1.add(s[r])                  # was s1 += s[r]
                max1 = max(max1, r - l + 1)   # update max when window is valid
                r += 1
            else:
                s1.remove(s[l])   # shrink window from left (don't reset)
                l += 1

        return max1
