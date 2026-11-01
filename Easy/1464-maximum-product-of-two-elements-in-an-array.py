/**
 * LeetCode #1464: Maximum Product of Two Elements in an Array
 * Difficulty: Easy
 * Language: Python3
 * Date: 2026-11-01T18:18:58.762Z
 */

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max1 = -float('inf')
        max2 = -float('inf')

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num                
            else:
                max2 = max(max2,num)
        return(max1 - 1) * (max2 - 1)