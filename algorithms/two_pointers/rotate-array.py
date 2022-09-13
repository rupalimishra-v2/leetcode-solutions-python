# https://leetcode.com/problems/rotate-array/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def numReverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k, n = k % len(nums), len(nums)

        if k:
            numReverse(0, n - 1)
            numReverse(0, k - 1)
            numReverse(k, n - 1)
        print(nums)


if __name__ == "__main__":
    nums, k = [1, 2, 3, 4, 5, 6, 7], 3
    print(Solution().rotate(nums, k))
