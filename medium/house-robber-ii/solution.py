"""
[Description]
House Robber II
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 
Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [1,2,3]
Output: 3

 
Constraints:

  1 <= nums.length <= 100
  0 <= nums[i] <= 1000

[Metadata]
- Difficulty: Medium
- Topics: Array, Dynamic Programming
- Slug: house-robber-ii
"""

// [Solution]
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Base cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # We solve the problem for two scenarios and return the max
        return max(self.rob_linear(nums[:-1]), self.rob_linear(nums[1:]))

    def rob_linear(self, houses):
        # This is the standard House Robber I logic
        if not houses:
            return 0
        if len(houses) == 1:
            return houses[0]
        
        total_loot = [0 for _ in range(len(houses))]
        total_loot[0] = houses[0]
        total_loot[1] = max(houses[0], houses[1])
        
        for i in range(2, len(houses)):
            # Decision: rob current (houses[i] + loot from 2 houses ago) 
            # OR skip current (loot from 1 house ago)
            total_loot[i] = max(total_loot[i-2] + houses[i], total_loot[i-1])
            
        return total_loot[-1]