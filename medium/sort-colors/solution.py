"""
[Description]
Sort Colors
https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

 
Constraints:

  n == nums.length
  1 <= n <= 300
  nums[i] is either 0, 1, or 2.

 
Follow up: Could you come up with a one-pass algorithm using only constant extra space?

[Metadata]
- Difficulty: Medium
- Topics: Array, Two Pointers, Sorting
- Slug: sort-colors
"""

// [Solution]
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        count0 = 0
        count1  = 0
        count2 = 0

        for i in nums:
            if i == 0 :
                count0+=1
            elif i ==1 :
                count1+=1
            else:
                count2+=1
            
        index = 0

        # overwrite array
        while count0 > 0:
            nums[index] = 0
            index += 1
            count0 -= 1

        while count1 > 0:
            nums[index] = 1
            index += 1
            count1 -= 1

        while count2 > 0:
            nums[index] = 2
            index += 1
            count2 -= 1