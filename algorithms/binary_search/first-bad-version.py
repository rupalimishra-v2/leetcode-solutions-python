# https://leetcode.com/problems/first-bad-version/submissions/

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version >= bad:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        first = 1
        last = n
        while last > first:
            mid = (first + last) // 2
            if isBadVersion(mid):
                last = mid
            else:
                first = mid + 1
        return first


if __name__ == "__main__":
    n = 5
    bad = 4
    print(Solution().firstBadVersion(n))
