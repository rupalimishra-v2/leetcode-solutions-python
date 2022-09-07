# Problem: https://leetcode.com/problems/contains-duplicate/

# Solution:
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = set()
        for i in nums:
            if i in a:
                return True
            else:
                a.add(i)
        return False


if __name__ == "__main__":
    nums = [1, 2, 2, 3]
    print(Solution().containsDuplicate(nums=nums))
