# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums) - 1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        return first


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    print(Solution().searchInsert(nums, target))
