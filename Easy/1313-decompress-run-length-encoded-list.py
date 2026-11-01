/**
 * LeetCode #1313: Decompress Run-Length Encoded List
 * Difficulty: Easy
 * Language: Python3
 * Date: 2026-11-01T16:09:47.662Z
 */

class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(0,len(nums),2):
            ans += [nums[i+1]]*nums[i]
        return ans