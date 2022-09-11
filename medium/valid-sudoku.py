# https://leetcode.com/problems/valid-sudoku/submissions/
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = sum(
            ([(c, i), (j, c), (i // 3, j // 3, c)]
             for i, row in enumerate(board)
             for j, c in enumerate(row)
             if c != '.')
            , [])
        [print(i) for i in seen]
        return len(seen) == len(set(seen))


if __name__ == "__main__":
    s = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],

         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],

         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]

    print(Solution().isValidSudoku(s))
