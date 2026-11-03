class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        ans = []
        for r in range(cols):
            row = []
            for c in range(rows):
                row.append(matrix[c][r])
            ans.append(row)
        
        return ans
