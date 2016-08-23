#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
熄灯问题：
• 有一个由按钮组成的矩阵, 其中每行有6个按钮, 共5行
• 每个按钮的位置上有一盏灯
• 当按下一个按钮后, 该按钮以及周围位置(上边, 下边, 左边, 右边)的灯都会改变一次
"""


class Solution(object):
    def lights_out(self, puzzle):
        """
        :type puzzle: List[int]
        :rtype: List[int]
        """

        def guess(press):
            for i in range(1, m):
                for j in range(1, n + 1):
                    press[i + 1][j] = (puzzle[i][j] + press[i][j] + press[i - 1][j] + press[i][j - 1] +
                                       press[i][j + 1]) % 2
            for i in range(1, n + 1):
                if (press[m][i - 1] + press[m][i] + press[m][i + 1] + press[m - 1][i]) % 2 != puzzle[m][i]: return False
            return True

        m, n = len(puzzle), len(puzzle[0])
        _puzzle = [[0] * (n + 2)]
        for p in puzzle: _puzzle.append([0] + p + [0])
        puzzle = _puzzle
        enum_count = 1 << n
        for i in range(enum_count):
            press = [[0] * (n + 2) for _ in range(m + 1)]
            temp = i
            for j in range(1, n + 1):
                press[1][j] = temp & 1
                temp >>= 1
            if guess(press):
                _press = []
                for i in range(1, m + 1): _press.append(press[i][1:-1])
                return _press


if __name__ == '__main__':
    solution = Solution()
    puzzle = [
        [0, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 1, 1],
        [0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 0]
    ]
    puzzle2 = [
        [0, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 1],
        [0, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0]
    ]
    press = solution.lights_out(puzzle)
    press2 = solution.lights_out(puzzle2)
    for p in press: print(p)
    for p in press2: print(p)
