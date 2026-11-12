class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        db = {}
        for num in nums:
            if num not in db:
                db[num] = 1
            else:
                db[num] += 1
        ans = 0

        for num, cnt in db.items():
            if cnt == 1:
                ans += num
        return ans

        # counter = Counter.{}

        # for num, cnt in counter.items():
        #     if cnt == 1:
        #         ans += num
        # return ans