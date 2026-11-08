class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        minprice = float('inf')

        for p in prices:
            minprice = min(p,minprice)
            ans = max(ans,p - minprice)
        return ans
