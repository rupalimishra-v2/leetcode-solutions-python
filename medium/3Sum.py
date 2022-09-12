# https://leetcode.com/problems/3sum/

from itertools import combinations
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n, p, z = [], [], []
        for num in nums:
            if num < 0:
                n.append(num)
            elif num > 0:
                p.append(num)
            else:
                z.append(num)

        N, P = set(n), set(p)
        if z:
            for x in N:
                if -x in P:
                    res.add((x, 0, -x))

        if len(z) >= 3:
            res.add((0, 0, 0))

        for x, y in combinations(n, 2):
            target = -1 * (x + y)
            if target in P:
                res.add(tuple(sorted((x,y,target))))

        for x, y in combinations(p, 2):
            target = -1 * (x + y)
            if target in N:
                res.add(tuple(sorted((x,y,target))))

        return [list(x) for x in res]


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
