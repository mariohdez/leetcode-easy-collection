import sys
from typing import List


class PlusOneSolution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1

        while i > -1 and carry != 0:
            result = digits[i] + carry
            carry = result // 10
            digits[i] = result % 10
            i = i - 1

        if carry != 0:
            digits.insert(0, carry)

        return digits
