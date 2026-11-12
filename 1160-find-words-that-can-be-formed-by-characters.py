class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars_cnt = Counter(chars)

        ans = 0

        for w in words:
            ans += len(w) if chars_cnt >= Counter(w) else 0
        return ans
            
        