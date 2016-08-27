#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
烘晾衣服:
现有 n 件衣服需要烘干, 每件衣服的含水量为 ai
• 如果自然晾干, 每分钟含水量减少 1
• 如果使用烘干机烘干, 每分钟含水量减少 k (直至为0)
只有一台烘干机, 每次只能烘干一件衣服且一次至少使用1分钟, 求使所有衣服含水量为0的最少时间是多少

问题转换:
最小值问题  判定性问题   判断在时间X内, 是否能晾干/烘干所有的衣服
"""


class Solution(object):
    def bake_dry_clothes(self, clothes, k):
        """
        :type clothes: List[int]
        :type k: int
        :rtype: int
        """

        def check(time):
            used = 0
            for c in clothes:
                if c > time:
                    # ceil(a/b) == (a-1)//b + 1
                    used += (c - time - 1) // (k - 1) + 1
                    if used > time: return False
            return True

        max_val = max(clothes)
        if k == 1: return max_val
        left, right = 0, max_val
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solution = Solution()
    clothes = [2, 3, 9]
    print(solution.bake_dry_clothes(clothes, 5))
