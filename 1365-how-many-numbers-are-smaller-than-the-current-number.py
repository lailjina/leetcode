class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        db = {}

        nums_sorted = sorted(nums)

        for i, num in enumerate(nums_sorted):
            if num not in db:
                db[num] = i

        for num in nums:
            ans.append(db[num])
        return ans
