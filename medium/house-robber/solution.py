"""
[Description]
House Robber
https://leetcode.com/problems/house-robber/

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
        total_loot = [1 for _ in range(len(nums))]
        total_loot[0]=nums[0]
        total_loot[1]=max(nums[0], nums[1])
        for i in range(2,len(nums)):
            #if i rob the house , that means that till n-2 th index i had robbed 
            #if i dont rob it the i wuld have robbed till n-1 or the previous one
            total_loot[i] = max(total_loot[i-2]+nums[i], total_loot[i-1])
        return total_loot[-1]

                

