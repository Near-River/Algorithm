#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
讨厌的青蛙
• 在韩国, 有一种小青蛙, 每到晚上, 这种青蛙会跳跃稻田, 从而踩踏稻子
• 农民早上看到被踩踏的稻子, 希望找到造成最大损害的那只青蛙经过的路径
• 每只青蛙总是沿着一条直线跳跃稻田, 且每次跳跃的距离都相同
稻田里的稻子组成一个栅格, 每棵稻子位于一个格点上, 而青蛙总是从稻田的一侧跳进稻田, 然后沿着某条直线穿越稻田, 从另一侧跳出去
可能会有多只青蛙从稻田穿越, 青蛙每一跳都恰好踩在一棵水稻上, 将这棵水稻拍倒, 有些水稻可能被多只青蛙踩踏
而在一条青蛙行走路径的直线上, 也可能会有些被踩踏的水稻不属于该行走路径

请写一个程序, 确定:
• 在各条青蛙行走路径中, 踩踏水稻最多的那一条上, 有多少颗水稻被踩踏
"""


class Plant(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution(object):
    def find_longest_path(self, plants, height, width):
        """
        :type plants: List[Plant]
        :type height: int
        :type width: int
        :rtype: int
        """

        def search_path(plant, dx, dy):
            steps = 2
            x, y = plant.x + dx, plant.y + dy
            while 0 <= x < height and 0 <= y < width:
                if (x, y) not in map: return 2
                x += dx
                y += dy
                steps += 1
            return steps

        n = len(plants)
        longest_path = -1
        map = {}  # 使用哈希表来存储水稻坐标信息，可以使用二分查询来优化搜索
        for p in plants: map[(p.x, p.y)] = True
        # 将水稻按x坐标从小到大排序, x坐标相同按y从小到大排序
        plants = sorted((sorted(plants, key=lambda p: p.y)), key=lambda p: p.x)
        for i in range(n - 2):
            pi = plants[i]
            for j in range(i + 1, n):
                pj = plants[j]
                dx, dy = pj.x - pi.x, pj.y - pi.y
                prevX, prevY = pi.x - dx, pi.y - dy
                if 0 <= prevX < height and 0 <= prevY < width: continue
                if pi.x + 2 * dx >= height: break
                nextY = pi.y + 2 * dy
                if nextY < 0 or nextY >= width: continue
                steps = search_path(pj, dx, dy)
                if steps > 2: longest_path = max(longest_path, steps)
        return longest_path


if __name__ == '__main__':
    solution = Solution()
    plants = [
        Plant(1, 0), Plant(5, 5), Plant(3, 1),
        Plant(1, 4), Plant(1, 5), Plant(1, 6),
        Plant(2, 3), Plant(5, 0), Plant(5, 1),
        Plant(1, 2), Plant(5, 2), Plant(5, 3),
        Plant(5, 4), Plant(5, 6)
    ]
    print(solution.find_longest_path(plants, height=6, width=7))
