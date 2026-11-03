class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        ans = 0
        n = len(mat)

        c = 0
        for r in range(n):
            ans += mat[r][c]
            c += 1

        c = n - 1
        for r in range(n):
            if r != c:
                ans += mat[r][c]
            c -= 1
        
        return ans