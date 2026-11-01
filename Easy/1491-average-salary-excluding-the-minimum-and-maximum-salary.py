/**
 * LeetCode #1491: Average Salary Excluding the Minimum and Maximum Salary
 * Difficulty: Easy
 * Language: Python3
 * Date: 2026-11-01T14:43:15.657Z
 */

class Solution:
    def average(self, salary: list[int]) -> float:
        summ, lenn, minn, maxx = 0, 0, float('inf'), -float('inf')

        for s in salary:
            summ += s
            lenn += 1

            if s > maxx:
                maxx = s

            if s < minn:
                minn = s

        return (summ - minn - maxx) / (lenn - 2)

        