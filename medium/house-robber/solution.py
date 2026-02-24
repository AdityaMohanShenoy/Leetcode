"""
[Description]
House Robber
https://leetcode.com/problems/house-robber/submissions/1929646757/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

 
Constraints:

  1 <= nums.length <= 100
  0 <= nums[i] <= 400

[Metadata]
- Difficulty: Medium
- Topics: Array, Dynamic Programming
- Slug: house-robber
"""

// [Solution]
class Solution(object):
    def rob(self, nums):
        robbed_prev = 0
        free = 0

        for x in nums:
            new_robbed = free + x

            if free > robbed_prev:
                new_free = free
            else:
                new_free = robbed_prev

            robbed_prev = new_robbed
            free = new_free

        return robbed_prev if robbed_prev > free else free


                

