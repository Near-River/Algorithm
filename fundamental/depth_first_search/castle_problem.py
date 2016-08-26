#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
城堡问题：
    给出一个城堡的地形图。请你编写一个程序，计算城堡一共有多少房间，最大的房间有多大。
城堡被分割成m×n(m≤50，n≤50)个方块，每个方块可以有0~4面墙。

1表示西墙，2表示北墙，4表示东墙，8表示南墙。每个方块用代表其周围墙的数字之和表示。
"""


class Solution(object):
    def castle_problem(self, board):
        """
        :type board: List[List[int]]
        :rtype: void
        """

        def dfs(i, j):
            if board[i][j] < 0: return 0
            val, roomArea = board[i][j], 1
            board[i][j] = -1 * roomCount
            if val & 1 == 0: roomArea += dfs(i, j - 1)
            if val & 2 == 0: roomArea += dfs(i - 1, j)
            if val & 4 == 0: roomArea += dfs(i, j + 1)
            if val & 8 == 0: roomArea += dfs(i + 1, j)
            return roomArea

        m, n = len(board), len(board[0])
        roomCount, maxRoomArea = 0, 0

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    roomCount += 1
                    maxRoomArea = max(maxRoomArea, dfs(i, j))
        print('RoomNums: %s, MaxRoomArea: %s' % (roomCount, maxRoomArea))


if __name__ == '__main__':
    solution = Solution()
    board = [
        [11, 6, 11, 6, 3, 10, 6],
        [7, 9, 6, 13, 5, 15, 5],
        [1, 10, 12, 7, 13, 7, 5],
        [13, 11, 10, 8, 10, 12, 13]
    ]
    solution.castle_problem(board)
