#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Michael喜欢滑雪这并不奇怪， 因为滑雪的确很刺激。
可是为了获得速度，滑的区域必须向下倾斜，而且当你滑到坡底，你不得不再次走上坡或者等待升降机来载你。
Michael想知道一个区域中最长的滑坡。区域由一个二维数组给出。数组的每个数字代表点的高度。

L(i,j)表示从点(i,j)出发的最长滑行长度。
一个点(i,j), 如果周围没有比它低的点，L(i,j) = 1
否则 递推公式： L(i,j) 等于(i,j)周围四个点中,比(i,j)低，且L值最大的那个点的L值，再加1

L(i,j)表示从点(i,j)出发的最长滑行长度。
一个点(i,j), 如果周围没有比它低的点，L(i,j) = 1
将所有点按高度从小到大排序。每个点的 L 值都初始化为1
从小到大遍历所有的点。经过一个点(i,j)时，要更新他周围的，比它高的点的L值。
例如： if H(i+1,j) > H(i,j): L(i+1,j) = max(L(i+1,j),L(i,j)+1)
"""


class Solution(object):
    def skliing(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        dp = [[1] * n for _ in range(m)]
        height = []
        for i in range(m):
            for j in range(n):
                height.append((i, j, board[i][j]))
        height = sorted(height, key=lambda x: x[2])
        ret = -1
        for (i, j, h) in height:  # '我为人人'式递推
            ret = max(ret, dp[i][j])
            if j + 1 < n and board[i][j + 1] > h:
                dp[i][j + 1] = max(dp[i][j] + 1, dp[i][j + 1])
            if i + 1 < m and board[i + 1][j] > h:
                dp[i + 1][j] = max(dp[i][j] + 1, dp[i + 1][j])
            if j - 1 >= 0 and board[i][j - 1] > h:
                dp[i][j - 1] = max(dp[i][j] + 1, dp[i][j - 1])
            if i - 1 >= 0 and board[i - 1][j] > h:
                dp[i - 1][j] = max(dp[i][j] + 1, dp[i - 1][j])
        return ret


if __name__ == '__main__':
    solution = Solution()
    board = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9],
    ]
    print(solution.skliing(board))
