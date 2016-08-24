#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
棋盘分割
将一个8*8的棋盘进行如下分割: 将原棋盘割下一块矩形棋盘并使剩下部分也是矩形, 再将剩下的部分继续如此分割, 这样割了(n-1)次后,
连同最后剩下的矩形棋盘共有n块矩形棋盘.(每次切割都只能沿着棋盘格子的边进行)

原棋盘上每一格有一个分值, 一块矩形棋盘的总分为其所含各格分值之和
现在需要把棋盘按上述规则分割成 n 块矩形棋盘, 并使各矩形棋盘总分的均方差最小
请编程对给出的棋盘及 n, 求出 σ 的最小值
"""
from math import sqrt


class Solution(object):
    def split_board(self, board, n):
        """
        :type board: List[List[int]]
        :rtype: n: int
        :rtype: int
        """

        def calculateSum(x1, y1, x2, y2):
            # (x1, y1)到(x2, y2)的矩形的分数之和
            return sum[x2][y2] - sum[x2][y1 - 1] - sum[x1 - 1][y2] + sum[x1 - 1][y1 - 1]

        def fun(n, x1, y1, x2, y2):
            _min = 1 << 31
            if n == 1: return calculateSum(x1, y1, x2, y2) ** 2
            c = x1
            while c < x2:
                part1, part2 = calculateSum(x1, y1, c, y2), calculateSum(c + 1, y1, x2, y2)
                temp = min(fun(n - 1, x1, y1, c, y2) + part2 ** 2, fun(n - 1, c + 1, y1, x2, y2) + part1 ** 2)
                _min = min(_min, temp)
                c += 1
            r = y1
            while r < y2:
                part1, part2 = calculateSum(x1, y1, x2, r), calculateSum(x1, r + 1, x2, y2)
                temp = min(fun(n - 1, x1, y1, x2, r) + part2 ** 2, fun(n - 1, x1, r + 1, x2, y2) + part1 ** 2)
                _min = min(_min, temp)
                r += 1
            return _min

        m = len(board)
        board.insert(0, [0] * (m + 1))
        for i in range(1, m + 1): board[i].insert(0, 0)
        sum = [[0] * (m + 1) for _ in range(m + 1)]  # (0, 0)到(i, j)的矩形的分数之和
        for i in range(1, m + 1):
            rowSum = 0
            for j in range(m + 1):
                rowSum += board[i][j]
                sum[i][j] = sum[i - 1][j] + rowSum

        sigma = sqrt((n * fun(n, 1, 1, m, m) - sum[m][m] ** 2) / (n ** 2))
        return sigma


if __name__ == '__main__':
    solution = Solution()
    board = [
        [1, 1, 1, 1, 1, 1, 1, 3],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 0, 3]
    ]
    print(solution.split_board(board, n=3))
