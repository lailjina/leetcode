/**
 * LeetCode #605: Can Place Flowers
 * Difficulty: Easy
 * Language: Python3
 * Date: 2026-11-01T15:20:08.971Z
 */

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if not sum(flowerbed[i-1:i+2]):
                flowerbed[i] = 1
                n -= 1

        return n <= 0