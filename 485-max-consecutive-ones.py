class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        cur = 0
        ans = 0

        for num in nums:
            if num == 1:
                cur += 1
                ans = max(cur,ans)
            else:            
                cur = 0
        return ans