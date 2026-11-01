/**
 * LeetCode #724: Find Pivot Index
 * Difficulty: Easy
 * Language: Python3
 * Date: 2026-11-01T18:47:51.373Z
 */

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        right = sum(nums)

        for i in range(len(nums)):
            if (left == right-nums[i]):
                return i
            left += nums[i]
            right -= nums[i]
        return -1