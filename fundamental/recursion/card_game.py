#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
小游戏
• 游戏在一个分割成 w * h 个正方格子的矩形板上进行
• 每个正方格子上可以有一张游戏卡片, 当然也可以没有

当下面的情况满足时,认为两个游戏卡片之间有一条路径相连:
• 路径只包含水平或者竖直的直线段
• 路径不能穿过别的游戏卡片
• 但是允许路径临时的离开矩形板
"""


class Solution(object):
    def find_longest_path(self, board, start, end):
        """
        :type board: List[List[str]]
        :rtype: start: Tuple
        :rtype: end: Tuple
        :rtype: int
        """

        def search_path(currX, currY, endX, endY, steps, direction):
            if steps > self.min_steps: return
            if currX == endX and currY == endY:
                self.min_steps = min(self.min_steps, steps)
            else:
                for i in range(4):
                    x, y = currX + Direction[i][0], currY + Direction[i][1]
                    if (0 <= x < m and 0 <= y < n) and (
                                (board[x][y] == ' ' and mark[x][y] == False) or (
                                                board[x][y] == 'X' and x == endX and y == endY)):
                        mark[x][y] = True
                        if i == direction:
                            search_path(x, y, endX, endY, steps, i)
                        else:
                            search_path(x, y, endX, endY, steps + 1, i)
                        mark[x][y] = False

        m, n = len(board) + 2, len(board[0]) + 2
        _board = [[' '] * n]
        for b in board: _board.append([' '] + b + [' '])
        _board.append([' '] * n)
        board = _board
        mark = [[False] * n for _ in range(m)]
        Direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.min_steps = 100000
        search_path(start[0] + 1, start[1] + 1, end[0] + 1, end[1] + 1, steps=0, direction=-1)
        if self.min_steps < 100000:
            print('Segments: %d' % self.min_steps)
        else:
            print('Impossible')


if __name__ == '__main__':
    solution = Solution()
    board = [
        ['X', 'X', 'X', 'X', 'X'],
        ['X', ' ', ' ', ' ', 'X'],
        ['X', 'X', 'X', ' ', 'X'],
        [' ', 'X', 'X', 'X', ' ']
    ]
    solution.find_longest_path(board, start=(2, 1), end=(2, 4))
    solution.find_longest_path(board, start=(2, 0), end=(3, 3))
    solution.find_longest_path(board, start=(2, 1), end=(3, 2))
