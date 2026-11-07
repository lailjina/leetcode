class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        cur = 0
        ans = 0
        prev = -float('inf')

        for num in nums:
            if num > prev:
                cur += 1                                          
            else:
                cur = 1
                
            prev = num
            ans = max(cur,ans) 
        return ans