#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
生日蛋糕:
    要制作一个体积为Nπ 的M层生日蛋糕，每层都是一个圆柱体。设从下往上数第i(1 <= i <= M)层蛋糕是半径为R i ,
高度为H i 的圆柱。当i < M时，要求R i > R i+1 且H i > H i+1 。由于要在蛋糕上抹奶油，为尽可能节约经费，我们
希望蛋糕外表面（最下一层的下底面除外）的面积Q最小。
令Q = Sπ, 请编程对给出的N和M，找出蛋糕的制作方案（适当的Ri和Hi的值），使S最小。

剪枝
1：搭建过程中发现面积超过已经求得的最优表面积，则停止搭建
2：搭建过程中预见到再往上搭，高度已经无法安排，或者半径已经无法安排，则停止搭建
3：搭建过程中发现还没搭的那些层的体积，一定会超过还缺的体积，则停止搭建
4：搭建过程中发现还没搭的那些层的体积，最大也到不了还缺的体积，则停止搭建
"""
from math import sqrt


class Solution(object):
    def birthday_cake(self, N, M):
        """
        :type N: int
        :type M: int
        :rtype: int
        """

        def dfs(v, n, maxH, maxR):
            if n == 0:
                if v == 0: self.minSurface = min(self.minSurface, self.currS)
                return
            if v <= 0: return

            if self.currS + minS[n] >= self.minSurface: return  # 剪枝一
            if maxH < n or maxR < n: return  # 剪枝二
            if v < minV[n]: return  # 剪枝三
            _v = 0
            for i in range(n): _v += (maxH - i) * (maxR - i) ** 2  # 剪枝四
            if _v < v: return

            for r in range(maxR, n - 1, -1):
                if n == M: self.currS = r * r
                for h in range(maxH, n - 1, -1):
                    self.currS += 2 * h * r
                    dfs(v - r * r * h, n - 1, h - 1, r - 1)
                    self.currS -= 2 * h * r

        self.minSurface = Infinite = 1 << 31 - 1
        minV = [0] * (M + 1)  # minV[n] 表示 n 层蛋糕最少的体积
        minS = [0] * (M + 1)  # minS[n] 表示 n 层蛋糕最少的侧表面积
        for i in range(1, M + 1):
            minV[i] = minV[i - 1] + i ** 3
            minS[i] = minS[i - 1] + 2 * i * i

        if minV[M] > N: return -1
        maxH = (N - minV[M - 1]) // (M * M) + 1
        maxR = int(sqrt((N - minV[M - 1]) // M)) + 1
        self.currS = 0  # 当前蛋糕的表面积
        dfs(N, M, maxH, maxR)
        if self.minSurface < Infinite: return self.minSurface
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.birthday_cake(1, 1))
