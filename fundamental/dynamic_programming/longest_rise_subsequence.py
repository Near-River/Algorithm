#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
最长上升子序列:
一个数的序列ai，当a 1 < a 2 < ... < a S 的时候，我们称这个序列是上升的。对于给定的一个序列(a 1 , a 2 , ..., a N )，
我们可以得到一些上升的子序列(a i1 , a i2 , ..., a iK )，这里1 <= i1 <i2 < ... < iK <= N。比如，对于序列(1, 7, 3, 5, 9, 4, 8)，
有它的一些上升子序列，如(1, 7), (3, 4, 8)等等。这些子序列中最长的长度是4，比如子序列(1, 3, 5, 8).
你的任务，就是对于给定的序列，求出最长上升子序列的长度。
"""


class Solution(object):
    def longest_rise_subsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 求以nums[k] （k=0, 2, 3 … n-1）为终点的最长上升子序列的长度
        ret = 1
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ret = max(ret, dp[i])
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.longest_rise_subsequence([1, 7, 3, 5, 9, 4, 8]))
