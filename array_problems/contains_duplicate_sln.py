from typing import List

class ContainsDuplicateSln:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        # Sliding window of length 2.
        for right in range(1, len(nums)):
            left = right - 1

            if nums[right] - nums[left] == 0:
                return True

        return False
