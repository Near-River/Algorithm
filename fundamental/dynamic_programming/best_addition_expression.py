#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
最佳加法表达式:
有一个由1..9组成的数字串.问如果将m个加号插入到这个数字串中,在各种可能形成的表达式中，值最小的那个表达式的值是多少

设V(m,n)表示在n个数字中插入m个加号所能形成的表达式最小值，那么：
if m = 0
    V(m,n) = n个数字构成的整数
else if n < m + 1
    V(m,n) = ∞
else
    V(m,n) = Min{ V(m-1,i) + Num(i+1,n) } ( i = m … n-1)
Num(i,j)表示从第i个数字到第j个数字所组成的数。数字编号从1开始算。
"""


class Solution(object):
    def best_addition_expression(self, s, m):
        """
        :type s: str
        :type m: int
        :rtype: int
        """
        n = len(s)
        if n < m + 1: return -1
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        for i in range(1, n + 1): dp[0][i] = int(s[:i])

        for i in range(1, m + 1):
            for j in range(i + 1, n + 1):
                _min = -1
                for k in range(i, j):
                    temp = dp[i - 1][k] + int(s[k:j])
                    if _min == -1 or temp < _min: _min = temp
                dp[i][j] = _min

        # for d in dp: print(d)
        return dp[m][n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.best_addition_expression('38293617', 3))
