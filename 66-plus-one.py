class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 1

        for i in range(len(digits)-1,-1,-1):
            cur = digits[i] + carry

            d = cur % 10
            carry = cur // 10

            digits[i] = d

        if carry > 0:
            digits = [carry] + digits
        return digits

