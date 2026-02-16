"""
[Description]
Construct K Palindrome Strings
https://leetcode.com/problems/construct-k-palindrome-strings/

Given a string s and an integer k, return true if you can use all the characters in s to construct non-empty k palindrome strings or false otherwise.

 
Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.

Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.

 
Constraints:

  1 <= s.length <= 105
  s consists of lowercase English letters.
  1 <= k <= 105

[Metadata]
- Difficulty: Medium
- Topics: Hash Table, String, Greedy, Counting
- Slug: construct-k-palindrome-strings
"""

// [Solution]
class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:  # If the string length is less than k, return False
            return False
        
        # Create a frequency dictionary
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1  # Increment count for each character
        
        # Count the number of characters with odd frequencies
        odd = 0
        for freq in count.values():
            odd += freq % 2  # Increment odd if the frequency is odd
        
        # If the number of odd frequencies is less than or equal to k, return True
        return odd <= k
