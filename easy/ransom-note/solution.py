"""
[Description]
Ransom Note
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

 
Constraints:

  1 <= ransomNote.length, magazine.length <= 105
  ransomNote and magazine consist of lowercase English letters.

[Metadata]
- Difficulty: Easy
- Topics: Hash Table, String, Counting
- Slug: ransom-note
"""

// [Solution]
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        s1 = ''.join(sorted(ransomNote))
        s2 = ''.join(sorted(magazine))

        i = 0  
        j = 0  

        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1

        return i == len(s1)
