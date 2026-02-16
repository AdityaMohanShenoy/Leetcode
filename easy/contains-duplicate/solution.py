"""
[Description]
Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 
Constraints:

  1 <= nums.length <= 105
  -109 <= nums[i] <= 109

[Metadata]
- Difficulty: Easy
- Topics: Array, Hash Table, Sorting
- Slug: contains-duplicate
"""

// [Solution]
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n1= sorted(nums)
        # print(n1)
        # i=0
        # while(i<len(nums)-1):
        #     if(n1[i]==n1[i+1]):
        #         return True
        #     else:
        #         i=i+1
        # return False
        s1=set(nums)
        s2=list(s1)
        if(len(s2)==len(nums)):
            return False
        return True
        

