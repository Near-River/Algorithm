#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给出两个字符串，求出这样的一个最长的公共子序列的长度：
子序列中的每个字符都能在两个原串中找到，而且每个字符的先后顺序和原串中的先后顺序一致。
"""


class Solution(object):
    def longest_common_subsequence(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        len1, len2 = len(s1), len(s2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longest_common_subsequence('abcfbc', 'abfcab'))
    print(solution.longest_common_subsequence('programming', 'contest'))
    print(solution.longest_common_subsequence('abcd', 'mnp'))
