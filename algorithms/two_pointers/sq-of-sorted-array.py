# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0 for _ in nums]
        i, j = 0, len(nums) - 1
        for k in range(len(nums) - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                result[k] = nums[i] ** 2
                i += 1
            else:
                result[k] = nums[j] ** 2
                j -= 1
        return result


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    print(Solution().sortedSquares(nums))
