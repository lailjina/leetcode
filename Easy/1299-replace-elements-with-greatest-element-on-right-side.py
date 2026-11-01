/**
 * LeetCode #1299: Replace Elements with Greatest Element on Right Side
 * Difficulty: Easy
 * Language: Python3
 * Date: 2026-11-01T17:18:59.448Z
 */

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        maxx = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = maxx
            maxx = max(maxx, temp)
        return arr