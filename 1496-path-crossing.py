class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x,y = 0,0
        visited = {(x,y)}

        for s in path:
            if s == 'N':
                dx, dy = 0, 1
            elif s == 'S':
                dx, dy = 0, -1
            elif s == 'E':
                dx, dy = 1, 0
            elif s == 'W':
                dx, dy = -1, 0

            x += dx
            y += dy

            if (x,y) in visited:
                return True
            visited.add((x,y))
        return False
