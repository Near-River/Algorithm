#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
在上面的数字三角形中寻找一条从顶部到底边的路径，使得路径上所经过的数字之和最大。
路径上的每一步都只能往左下或右下走。只需要求出这个最大和即可，不必给出具体路径。
"""


class Solution(object):
    def triangle_path_sum(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + max(dp[j], dp[j + 1])
        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    triangle = [
        [7],
        [3, 8],
        [8, 1, 0],
        [2, 7, 4, 4],
        [4, 5, 2, 6, 5]
    ]
    print(solution.triangle_path_sum(triangle))
