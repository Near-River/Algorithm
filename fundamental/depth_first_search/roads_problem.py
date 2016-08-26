#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
寻路问题：
    N个城市，编号1到N。城市间有R条单向道路。每条道路连接两个城市，有长度和过路费两个属性。
Bob只有K块钱，他想从城市1走到城市N。问最短共需要走多长的路。如果到不了N，输出-1

优化：
1) 如果当前已经找到的最优路径长度为L ,那么在继续搜索的过程中，总长度已经大于L的走法，就可以直接放弃。
2) 用midL[k][m] 表示：走到城市k时总过路费为m的条件下，最优路径的长度。若在后续的搜索中，再次走到k时，
如果总路费恰好为m，且此时的路径长度已经超过midL[k][m],则不必再走下去了。
"""


class Solution(object):
    def roads_problem(self, N, K, roads):
        """
        :type N: int
        :type K: int
        :type roads: List[tuple]
        :rtype: int
        """

        def dfs(start, totalLen, totalCost):
            if start == N:
                self.minLen = min(self.minLen, totalLen)
                return
            if start in roadsMap:
                for (d, l, f) in roadsMap[start]:
                    if not visited[d]:
                        cost = totalCost + f
                        length = totalLen + l
                        if cost > K or length >= self.minLen: continue
                        if (d, cost) in midL and midL[(d, cost)] <= length: continue
                        midL[(d, cost)] = length
                        visited[d] = True
                        dfs(d, length, cost)
                        visited[d] = False

        midL = {}  # minL[(i, j)] 表示从1到i点的，花销为j的最短路径的长度
        self.minLen = Infinite = 1 << 31 - 1
        visited = [False] * (N + 1)
        roadsMap = {}
        for road in roads:
            s = road[0]
            if s in roadsMap:
                roadsMap[s].append(road[1:])
            else:
                roadsMap[s] = [road[1:]]

        visited[1] = True
        dfs(1, 0, 0)
        if self.minLen < Infinite: return self.minLen
        return -1


if __name__ == '__main__':
    solution = Solution()
    roads = [
        (1, 2, 10, 10),
        (2, 3, 10, 10),
        (2, 4, 15, 20),
        (3, 4, 10, 10)
    ]
    print(solution.roads_problem(4, 30, roads))
