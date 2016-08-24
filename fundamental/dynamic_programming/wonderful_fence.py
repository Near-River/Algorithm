#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
美妙的栅栏:
    N 个木棒, 长度分别为1, 2, …, N. 构成美妙的栅栏, 除了两端的木棒外，每一跟木棒，要么比它左右的两根都长，
要么比它左右的两根都短。即木棒呈现波浪状分布,这一根比上一根长了，那下一根就比这一根短，或反过来。

问题: 符合上述条件的栅栏建法有很多种，对于满足条件的所有栅栏, 按照字典序(从左到右, 从低到高)排序。
    给定一个栅栏的排序号，请输出该栅栏, 即每一个木棒的长度.

A[i] = ∑ B[i][k] k = 1….i   B[i][k] 是S(i)中以第k短的木棒打头的方案数。
B[i][k] = C[i][k][DOWN] + C[i][k][UP]   C[i][k][DOWN] 是S(i)中以第k短的木棒打头的DOWN方案数。
    C[i][k][UP] = ∑ C[i-1][M][DOWN]     M = k ... i -1
    C[i][k][DOWN] = ∑ C[i-1][N][UP]     N = 1… k-1
初始条件：C[1][1][UP] = C[1][1][DOWN] = 1
n根木棒的总方案数是 Sum{ C[n][k][DOWN] + C[n][k][UP] }   k = 1.. n;
"""


class Solution(object):
    def wonderful_fence(self, N, C):
        """
        :type N: int
        :type C: int
        :rtype: int
        """
        # 动归 + 排列计数
        DOWN, UP = 0, 1
        # dp[i][k][ UP]: 表示S(i)中以第k短的木棒打头的UP方案数。
        dp = [[[0, 0] for _ in range(N + 1)] for _ in range(N + 1)]
        dp[1][1][UP] = dp[1][1][DOWN] = 1
        for i in range(2, N + 1):
            for j in range(1, i + 1):
                for k in range(j, i):
                    dp[i][j][UP] += dp[i - 1][k][DOWN]
                for k in range(1, j):
                    dp[i][j][DOWN] += dp[i - 1][k][UP]

        ret = []
        used = [False] * (N + 1)  # 标记木棒是否使用过
        for i in range(1, N + 1):
            no = 0  # 标记i根木棒中的第no短的木棒
            k = 1
            while k <= N:
                skipped = 0  # 已经跳过的方案数
                if not used[k]:
                    no += 1
                    if i == 1:
                        skipped = dp[N][no][UP] + dp[N][no][DOWN]
                    else:
                        if k > ret[-1] and (i == 2 or ret[-2] > ret[-1]):
                            skipped = dp[N - i + 1][no][DOWN]
                        elif k < ret[-1] and (i == 2 or ret[-2] < ret[-1]):
                            skipped = dp[N - i + 1][no][UP]
                    if skipped >= C: break
                    C -= skipped
                k += 1
            used[k] = True
            ret.append(k)
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.wonderful_fence(3, 3))
    print(solution.wonderful_fence(5, 5))
