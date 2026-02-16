"""
[Description]
Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 
Constraints:

  1 <= strs.length <= 200
  0 <= strs[i].length <= 200
  strs[i] consists of only lowercase English letters if it is non-empty.

[Metadata]
- Difficulty: Easy
- Topics: Array, String, Trie
- Slug: longest-common-prefix
"""

// [Solution]
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            ch = shortest[i]
            for s in strs:
                if s[i] != ch:
                    return shortest[:i]

        return shortest
