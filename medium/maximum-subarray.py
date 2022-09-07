# https://leetcode.com/problems/maximum-subarray/
import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -sys.maxsize
        sum = 0
        for i in nums:
            sum += i
            if sum < i:
                sum = i
            max_sum = max(max_sum, sum)
        return max_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums=nums))

