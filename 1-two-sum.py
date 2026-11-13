class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        db = {}

        for i, num in enumerate(nums):
            db[num] = i
        for i, num in enumerate(nums):
            pair = target - num
            if pair in db and db[pair] != i:
                return [db[pair],i]
