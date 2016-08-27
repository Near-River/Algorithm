#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
圣诞老人的礼物:
圣诞节来临了, 在城市A中圣诞老人准备分发糖果,现在有多箱不同的糖果
• 每箱糖果有自己的价值和重量
• 每箱糖果都可以拆分成任意散装组合带走
圣诞老人的驯鹿最多只能承受一定重量的糖果, 请问圣诞老人最多能带走 多大价值 的糖果
"""


class Solution(object):
    def santa_gifts(self, W, boxes):
        """
        :type W: int
        :type boxes: List[tuple]
        :rtype: void
        """

        class Candy(object):
            def __init__(self, v, w):
                self.v = v
                self.w = w
                self.density = self.v / self.w

        candies = []
        for (v, w) in boxes: candies.append(Candy(v, w))
        candies = sorted(candies, key=lambda c: c.density, reverse=True)
        totalV = totalW = 0
        for candy in candies:
            if totalW + candy.w < W:
                totalW += candy.w
                totalV += candy.v
            else:
                totalV += (W - totalW) * candy.density
                break
        print('MAX_VALUE: %.1f' % totalV)


if __name__ == '__main__':
    solution = Solution()
    boxes = [
        (100, 4), (412, 8), (266, 7), (591, 2)
    ]
    solution.santa_gifts(15, boxes)
