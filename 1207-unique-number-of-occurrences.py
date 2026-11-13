class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arr_cnt = Counter(arr)
        seen = set()

        for key, value in arr_cnt.items():
            if value in seen:
                return False
            seen.add(value)
        return True


