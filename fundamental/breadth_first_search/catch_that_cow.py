#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
抓住那头牛:
    农夫知道一头牛的位置，想要抓住它。农夫和牛都位于数轴上，农夫起始位于点N(0<=N<=100000)，牛位于点K(0<=K<=100000)。
农夫有两种移动方式：
  1、从X移动到X-1或X+1，每次移动花费一分钟
  2、从X移动到2*X，每次移动花费一分钟
假设牛没有意识到农夫的行动，站在原地不动。农夫最少要花多少时间才能抓住牛？
"""
from queue import Queue


class Solution(object):
    def catch_that_cow(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        MaxBoard = 100000
        visited = {}
        queue = Queue()
        queue.put((N, 0))
        visited[N] = True
        while not queue.empty():
            idx, step = queue.get()
            if idx == K: return step
            if idx - 1 >= 0 and (idx - 1) not in visited:
                queue.put((idx - 1, step + 1))
                visited[idx - 1] = True
            if idx + 1 <= MaxBoard and (idx + 1) not in visited:
                queue.put((idx + 1, step + 1))
                visited[idx + 1] = True
            if 2 * idx <= MaxBoard and 2 * idx not in visited:
                queue.put((2 * idx, step + 1))
                visited[2 * idx] = True
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.catch_that_cow(3, 5))
