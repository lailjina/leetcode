class Solution:
    def firstUniqChar(self, s: str) -> int:
        db = {}

        for c in s:
            if c not in db:
                db[c] = 1
            else:
                db[c] += 1 
        for i, c in enumerate(s):
            if db[c] == 1:
                return i
        return -1
                

