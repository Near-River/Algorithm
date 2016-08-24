#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
方盒游戏:
 N个方盒摆成一排，每个方盒有自己的颜色。连续摆放的同颜色方盒构成一个“大块”(Block)。
 玩家每次点击一个方盒，则该方盒所在大块就会消失。若消失的大块中共有k个方盒，则玩家获得k*k个积分。
 请问：给定游戏开始时的状态，玩家可获得的最高积分是多少？

click_box(i, j, ex_len)表示:
大块j的右边已经有一个长度为ex_len的大块(该大块可能是在合并过程中形成的，不妨就称其为ex_len)，且j的颜色和ex_len相同，
在此情况下将 i 到 j 以及ex_len都消除所能得到的最高分。

求click_box(i,j,ex_len)时，有两种处理方法，取最优者
假设j和ex_len合并后的大块称作 Q
1) 将Q直接消除，这种做法能得到的最高分就是：click_box(i,j-1,0) + (len[j]+ex_len)**2
2) 期待Q以后能和左边的某个同色大块合并。需要枚举可能和Q合并的大块。
   假设让大块k和Q合并，则此时能得到的最大分数是：click_box(i,k,len[j]+ex_len) + click_box(k+1,j-1,0)
"""


class Block(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def __str__(self):
        return 'Block: %s, %s' % (self.color, self.size)


class Solution(object):
    def box_game(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """

        def click_box(start, end, ex_len):
            # 使用记忆递归式
            if dp[start][end][ex_len] > 0: return dp[start][end][ex_len]
            color = blocks[end].color
            length = blocks[end].size
            result = (length + ex_len) ** 2
            if start == end:
                dp[start][end][ex_len] = result
                return result
            result += click_box(start, end - 1, 0)
            for i in range(end - 1, start - 1, -1):
                if blocks[i].color != color: continue
                temp = click_box(start, i, length + ex_len) + click_box(i + 1, end - 1, 0)
                if temp > result: result = temp
            dp[start][end][ex_len] = result
            return result

        n = len(boxes)
        blocks = []
        count = 0  # 大块的计算器
        color = boxes[0]  # 当前大块的颜色
        blocks.append(Block(color, 1))
        for i in range(1, n):
            if boxes[i] == color:
                blocks[count].size += 1
            else:
                count += 1
                color = boxes[i]
                blocks.append(Block(color, 1))
        dp = [[[0] * (n + 1) for _ in range(count + 1)] for _ in range(count + 1)]
        return click_box(0, count, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.box_game([1, 2, 2, 2, 2, 3, 3, 3, 4]))
    print(solution.box_game([1, 2, 2, 2, 2, 3, 3, 3, 4, 2, 2]))
