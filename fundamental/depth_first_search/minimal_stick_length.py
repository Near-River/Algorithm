#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
输入：N节木棒的长度。
输出：能拼成的最小的棍子长度。

状态可以是一个二元组 (R, M)
R : 还没被用掉的木棒数目。     M : 当前正在拼的棍子还缺少的长度。

剪枝方案：
1. 不要在同一个位置多次尝试相同长度的木棒。
2. 如果由于以后的拼接失败，需要重新调整第i根棍子的拼法，则不会考虑替换第i根棍子中的第一根木棒（换了也没用）。
   如果在不替换第一根木棒的情况下怎么都无法成功，那么就要推翻第i-1根棍子的拼法。如果不存在第i-1根棍子，那么就
   推翻本次假设的棍子长度，尝试下一个长度。
3. 不要希望通过仅仅替换已拼好棍子的最后一根木棒就能够改变失败的局面。
4. 拼每一根棍子的时候，应该确保已经拼好的部分，长度是从长到短排列的。
"""


class Solution(object):
    def minimal_stick_length(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """

        def dfs(left, lack):
            if left == lack == 0: return True
            if lack == 0: lack = self.L  # 已经拼接好一根，开始拼接下一根
            if lack == self.L: self.lastStickNo = -1
            for i in range(self.lastStickNo + 1, n):
                if not used[i] and sticks[i] <= lack:
                    if i > 0 and sticks[i] == sticks[i - 1] and not used[i - 1]: continue  # 剪枝一
                    used[i] = True
                    self.lastStickNo = i  # 剪枝四
                    if dfs(left - 1, lack - sticks[i]): return True
                    used[i] = False
                    if lack == sticks[i] or lack == self.L: return False  # 剪枝二、三

            return False

        n = len(sticks)
        used = [False] * n
        sticks = sorted(sticks, reverse=True)
        totalLen = sum(sticks)
        for l in range(sticks[0], totalLen // 2 + 1):
            if totalLen % l != 0: continue
            self.L = l
            self.lastStickNo = -1  # 记住最近拼上去的那条木棒的下标。
            if dfs(n, l): return l
        return totalLen


if __name__ == '__main__':
    solution = Solution()
    sticks = [46, 45, 36, 36, 36, 24, 19, 16, 14, 13]
    print(solution.minimal_stick_length(sticks))
