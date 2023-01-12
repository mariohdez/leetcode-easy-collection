import sys

class ReverseIntegerSolution:
    def reverse(self, x: int) -> int:
        reversedX = 0

        # Look at neetcode.io's solution because python has some weirdness with it's number data type implementation. #

        # while x > 0:
        #     remainder = x % 10

        #     if reversedX > sys.maxsize//10 or (reversedX == sys.maxsize//10 and remainder > 7):
        #         return 0
        #     if reversedX < (-sys.maxsize - 1)//10 or reversedX == (-sys.maxsize - 1)//10 and remainder < -8:
        #         return 0

        #     reversedX = (reversedX * 10) + remainder
        #     x = x // 10

        return reversedX
