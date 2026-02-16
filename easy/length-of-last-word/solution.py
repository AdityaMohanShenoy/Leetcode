"""
[Description]
Length of Last Word
https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

 
Constraints:

  1 <= s.length <= 104
  s consists of only English letters and spaces ' '.
  There will be at least one word in s.

[Metadata]
- Difficulty: Easy
- Topics: String
- Slug: length-of-last-word
"""

// [Solution]
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = 0
        length = 0
        
        # 1. Fixed Range: range(start, stop, step)
        # len(s)-1 is the last valid index.
        for i in range(len(s) - 1, -1, -1):
            
            # 2. Access the character using s[i], not just i
            char = s[i]
            
            if char == " ":
                if flag == 1:
                    # We already found a word and now hit a space: we're done!
                    return length
                else:
                    # Still trailing spaces at the very end, just skip them
                    continue
            else:
                # We found a non-space character
                length += 1 
                flag = 1
        
        return length