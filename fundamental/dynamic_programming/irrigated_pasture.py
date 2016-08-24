#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
灌溉草场:
在一片草场上:有一条长度为L (1 <= L <= 1,000,000，L为偶数)的线段。 John的N (1 <= N <= 1000) 头奶牛都沿着草场上这条线段吃草，
每头牛的活动范围是一个开区间(S,E)，S，E都是整数。不同奶牛的活动范围可以有重叠。
John要在这条线段上安装喷水头灌溉草场。每个喷水头的喷洒半径可以随意调节，调节范围是 [A B ](1 <= A <= B <= 1000)，A,B都是整数。
要求:
    线段上的每个整点恰好位于一个喷水头的喷洒范围内
    每头奶牛的活动范围要位于一个喷水头的喷洒范围内
    任何喷水头的喷洒范围不可越过线段的两端(左端是0,右端是L )
请问， John 最少需要安装多少个喷水头。

问题分析：
从线段的起点向终点安装喷水头，令f(X)表示：所安装喷水头的喷洒范围恰好覆盖直线上的区间[0 X]时，最少需要多少个喷水头
显然，X应满足下列条件
 X为偶数
 X所在位置不会出现奶牛，即X不属于任何一个(S,E)
 X>=2A
 当X>2B时，存在Y属于[X-2B X-2A]且Y满足上述三个条件，使得f(X)=f(Y)+1
"""

import heapq


class Fx(object):
    def __init__(self, i, f):
        self.i = i
        self.f = f

    def __gt__(self, other):
        return self.f > other.f

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.f == other.f

    def __str__(self):
        return 'Fx: %s, %s' % (self.i, self.f)


class Solution(object):
    def irrigated_pasture(self, L, cowRegions, A, B):
        """
        :type L: int
        :type cowRegions: List[tuple]
        :type A: int
        :type B: int
        :rtype: int
        """
        Infinite = 1 << 31
        n = len(cowRegions)
        A, B = A << 1, B << 1
        dp = [Infinite] * (L + 1)
        heap = []  # 存放Fx对象，按属性f进行从小到大排序

        cowThere = [0] * (L + 1)  # 表示当前点是否位于奶牛的活动范围
        for i in range(n):
            cowThere[cowRegions[i][0] + 1] += 1
            cowThere[cowRegions[i][1]] -= 1
        inCows = 0  # 表示当前点位于多少头奶牛的活动范围之内
        for i in range(L + 1):
            inCows += cowThere[i]
            cowThere[i] = inCows > 0
        i = A
        while i <= B:
            if not cowThere[i]:
                dp[i] = 1
                if i <= B - A + 2: heapq.heappush(heap, Fx(i, dp[i]))
            i += 2
        while i <= L:
            if not cowThere[i]:
                while heap:
                    fx = heap[0]
                    if fx.i < i - B:
                        heapq.heappop(heap)
                    else:
                        dp[i] = fx.f + 1
                        break
                if dp[i - A + 2] != Infinite: heapq.heappush(heap, Fx(i - A + 2, dp[i - A + 2]))
            i += 2
        if dp[L] == Infinite: return -1
        return dp[L]


if __name__ == '__main__':
    solution = Solution()
    cowRegions = [
        (6, 7), (3, 6)
    ]
    print(solution.irrigated_pasture(L=8, cowRegions=cowRegions, A=1, B=2))
