class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars_cnt = Counter(chars)

        ans = 0

        for w in words:
            w_cnt = Counter(w)
            good = True

            for c, cnt in w_cnt.items():
                if cnt > chars_cnt[c]:
                    good = False
            ans += len(w) if good else 0
        return ans
            
        