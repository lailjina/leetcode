class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        ans = 0

        for c in s:
            if c == 'L':
                balance += 1
            elif c == 'R':
                balance -= 1
            if balance == 0:
                ans += 1
        
        return ans