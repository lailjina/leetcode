class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_ransomNote = Counter(ransomNote)
        cnt_magazine = Counter(magazine)

        for c, cnt in cnt_ransomNote.items():
            if cnt_magazine[c] < cnt:
                return False
        return True 
