import math
import sys

class ReverseIntegerSolution:
    def reverse(self, x: int) -> int:
        reversedX = 0
        MIN = -2147483648
        MAX = 2147483647

        while x:
            remainder = int(math.fmod(x, 10))
            x = int(x / 10)

            if reversedX > MAX // 10 or (reversedX == MAX // 10 and remainder > 7):
                return 0
            if reversedX < MIN // 10 or (reversedX == MIN // 10 and  reversedX < -8):
                return 0
            reversedX = (reversedX * 10) + remainder

        return reversedX
