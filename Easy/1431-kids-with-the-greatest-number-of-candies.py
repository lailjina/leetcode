/**
 * LeetCode #1431: Kids With the Greatest Number of Candies
 * Difficulty: Easy
 * Language: Python3
 * Date: 2026-11-01T12:40:16.789Z
 */

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        
        return [c + extraCandies >= max_candies for c in candies]