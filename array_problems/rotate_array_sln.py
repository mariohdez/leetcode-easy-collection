from typing import List


class RotateArraySolution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if matrix is None:
            return None

        left = 0
        right = len(matrix) - 1
        bottom = len(matrix[0]) - 1
        top = 0

        while left < right and top < bottom:
            for i in range(right - left):
                value = matrix[top][left + i]

                temp = matrix[top + i][right]
                matrix[top + i][right] = value
                value = temp

                temp = matrix[bottom][right - i]
                matrix[bottom][right - i] = value
                value = temp

                temp = matrix[bottom - i][left]
                matrix[bottom - i][left] = value
                value = temp

                matrix[top][left + i] = value

            left = left + 1
            right = right - 1
            top = top + 1
            bottom = bottom - 1

        return None
