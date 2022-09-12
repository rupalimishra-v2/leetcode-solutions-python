from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums) - 1

        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
        print(nums)


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(Solution().sortColors(nums))
