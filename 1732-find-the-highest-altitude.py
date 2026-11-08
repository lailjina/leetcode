class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        ans = 0
        cur = 0

        for a in gain:
            cur += a    
            ans = max(cur,ans)
        return ans
            