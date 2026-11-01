/**
 * LeetCode #2574: Left and Right Sum Differences
 * Difficulty: Easy
 * Language: Python3
 * Date: 2026-11-01T18:30:05.800Z
 */

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return ans