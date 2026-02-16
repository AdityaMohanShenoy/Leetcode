"""
[Description]
Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

 
Constraints:

  1 <= haystack.length, needle.length <= 104
  haystack and needle consist of only lowercase English characters.

[Metadata]
- Difficulty: Easy
- Topics: Two Pointers, String, String Matching
- Slug: find-the-index-of-the-first-occurrence-in-a-string
"""

// [Solution]
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        
        n, m = len(haystack), len(needle)
        if m > n:
            return -1

        for start in range(n - m + 1):
            j = 0
            while j < m and haystack[start + j] == needle[j]:
                j += 1
            if j == m:
                return start

        return -1
