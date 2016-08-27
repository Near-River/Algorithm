#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
雷达安装问题:
 一共有n个小岛位于x轴之上, x轴为海岸, x轴上方为海洋, 现需要在海岸上建立雷达, 每个雷达的覆盖半径为d
也就是说每个雷达能覆盖距离它不超过d的所有点, 要求求出在海岸建立最少的雷达的数目, 使得可以覆盖所
有的小岛. 可以认为每个小岛都是一个点。
"""
from math import sqrt


class Solution(object):
    def installation_radar(self, islands, d):
        """
        :type islands: List[tuple]
        :type d: int
        :rtype: int
        """

        class RadarRange(object):
            def __init__(self, left, right):
                self.left = left
                self.right = right

        if not islands: return 0
        ranges = []
        for (x, y) in islands:
            if y > d: return -1
            temp = sqrt(float(d * d - y * y))
            ranges.append(RadarRange(x - temp, x + temp))

        ret = 1
        ranges = sorted(ranges, key=lambda r: r.left)
        now = ranges[0].right
        for i in range(1, len(ranges)):
            if ranges[i].left <= now:  # 若当前雷达区域与目前集合中的雷达区域有公共交点, 则更新右端点最小值
                now = min(now, ranges[i].right)
            else:  # 否则加入新雷达, 建立新集合
                ret += 1
                now = ranges[i].right
        return ret


if __name__ == '__main__':
    solution = Solution()
    islands = [
        (1, 2), (-3, 1), (2, 1)
    ]
    print(solution.installation_radar(islands, 2))
