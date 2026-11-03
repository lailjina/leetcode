class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for r in range(m - 1):
            for c in range(n - 1):
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
        
        return True