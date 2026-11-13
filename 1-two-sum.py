class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        db = {}

        for i, num in enumerate(nums):
            pair = target - num
            if pair in db:
                return [db[pair],i]
            db[num] = i
