class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed_set = set(allowed)

        for w in words:
            ans += 0 if set(w) - allowed_set else 1
            # cnt = 1
            # for c in w:
            #     if c not in allowed:
            #         cnt = 0
            # ans += cnt
        return ans


