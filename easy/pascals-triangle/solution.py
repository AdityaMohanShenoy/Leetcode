"""
[Description]
Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]

 
Constraints:

  1 <= numRows <= 30

[Metadata]
- Difficulty: Easy
- Topics: Array, Dynamic Programming
- Slug: pascals-triangle
"""

// [Solution]
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        output = [[numRows]]
        output[0] = [1]
        for i in range(1,numRows):
            prv_array = output[i-1]
            new_array = [0] * (len(prv_array) + 1)
            new_array[0] = 1
            new_array[-1] = 1
            

            p1 = 0 
            p2 = 1 
            k = 1 
            while (k < len(prv_array)):
                new_array[k] = prv_array[p1] + prv_array[p2]
                p1= p1+1
                p2 = p2+1
                k = k+1
            new_array[len(prv_array)]= 1

            output.append(new_array)
        
        return output


            







        