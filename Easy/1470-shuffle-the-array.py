/**
 * LeetCode #1470: Shuffle the Array
 * Difficulty: Easy
 * Language: Python3
 * Date: 2026-11-01T12:47:10.194Z
 */

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.extend([nums[i],nums[i+n]])            
        return ans