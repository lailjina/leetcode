class Solution:
    def addDigits(self, num: int) -> int:

        while num > 9:
            new_num = 0
            temp = num

            while temp:
                temp, d = divmod(temp,10)
                new_num += d
            num = new_num

        return num

