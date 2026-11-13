class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ans = 0
        db = Counter()

        for num in nums:
            ans += db[num]
            db[num] += 1
        return ans
