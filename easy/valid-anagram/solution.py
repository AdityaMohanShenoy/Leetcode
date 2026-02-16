"""
[Description]
Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 
Constraints:

  1 <= s.length, t.length <= 5 * 104
  s and t consist of lowercase English letters.

 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

[Metadata]
- Difficulty: Easy
- Topics: Hash Table, String, Sorting
- Slug: valid-anagram
"""

// [Solution]
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=sorted(s)
        t1=sorted(t)
        if(s1==t1):
            return True
        else:
            return False