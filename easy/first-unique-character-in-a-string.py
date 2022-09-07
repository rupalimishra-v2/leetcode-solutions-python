# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for l in s:
            if l not in d:
                d[l] = 1
            else:
                d[l] += 1

        index = -1
        for i in range(len(s)):
            print(d[s[i]])
            if d[s[i]] == 1:
                index = i
                break

        return index


if __name__ == "__main__":
    s = "leetcode"
    print(Solution().firstUniqChar(s))
