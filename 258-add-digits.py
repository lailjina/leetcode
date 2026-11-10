class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            temp = num
            new_num = 0

            while temp:
                temp, d = divmod(temp,10)
            
                new_num += d
            num = new_num
        return num
