#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
数读(sudoku)：
    将数字1到9,填入9x9矩阵中的小方格，使得矩阵中的每行，每列，每个3x3的小格子内，9个数字都会出现。
"""


class Solution(object):
    def sudoku(self, board):
        """
        :type board: List[List[int]]
        :rtype: void
        """

        def getBlockNum(r, c):
            return 3 * (r // 3) + c // 3

        def setAllFlags(r, c, idx, flag):
            rowFlags[r][idx] = flag
            colFlags[c][idx] = flag
            blockFlags[getBlockNum(r, c)][idx] = flag

        def isOkNumber(r, c, idx):
            return not rowFlags[r][idx] and not colFlags[c][idx] and not blockFlags[getBlockNum(r, c)][idx]

        def dfs(idx):
            if idx < 0: return True
            r, c = blanks[idx]
            for i in range(1, N + 1):
                if isOkNumber(r, c, i - 1):
                    board[r][c] = i
                    setAllFlags(r, c, i - 1, True)
                    if dfs(idx - 1): return True
                    setAllFlags(r, c, i - 1, False)
            return False

        N = 9
        rowFlags = [[False] * N for _ in range(N)]
        colFlags = [[False] * N for _ in range(N)]
        blockFlags = [[False] * N for _ in range(N)]
        blanks = []
        for r in range(N):
            for c in range(N):
                if board[r][c] == 0:
                    blanks.append((r, c))
                else:
                    setAllFlags(r, c, board[r][c] - 1, True)
        if dfs(len(blanks) - 1):
            for b in board: print(b)
        else:
            print('No Way.')


if __name__ == '__main__':
    solution = Solution()
    lst = [
        "103000509", "002109400", "000704000",
        "300502006", "060000050", "700803004",
        "000401000", "009205800", "804000107"
    ]
    board = []
    for l in lst: board.append(list(map(int, l)))
    solution.sudoku(board)
