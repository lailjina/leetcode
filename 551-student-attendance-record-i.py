class Solution:
    def checkRecord(self, s: str) -> bool:
        count_a = 0

        for c in s:
            if c == 'A':
                count_a += 1
            if count_a > 1:
                return False
        
        count_l = 0

        for c in s:
            if c == 'L':
                count_l += 1
                if count_l > 2:
                    return False
            else:
                count_l = 0

        return True      
