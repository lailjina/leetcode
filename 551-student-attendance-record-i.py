class Solution:
    def checkRecord(self, s: str) -> bool:
        count_a = 0
        count_l = 0

        for c in s:
            if c == 'A':
                count_a += 1
            if count_a > 1:
                return False
                        
            if c == 'L':
                count_l += 1
                if count_l > 2:
                    return False
            else:
                count_l = 0

        return True      
#   return (s.count('A') < 2 and 'LLL' not in s)