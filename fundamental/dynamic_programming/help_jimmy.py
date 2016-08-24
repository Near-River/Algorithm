#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Help Jimmy:
场景中包括多个长度和高度各不相同的平台。地面是最低的平台，高度为零，长度无限。
Jimmy老鼠在时刻0从高于所有平台的某处开始下落，它的下落速度始终为1米/秒。当Jimmy落到某个平台上时，游戏者选择让它
向左还是向右跑，它跑动的速度也是1米/秒。当Jimmy跑到平台的边缘时，开始继续下落。Jimmy每次下落的高度不能超过MAX米，
不然就会摔死，游戏也会结束。
设计一个程序，计算Jimmy到地面时可能的最早时间。
"""


class PlatForm(object):
    def __init__(self, lx, rx, h):
        self.lx = lx
        self.rx = rx
        self.h = h

    def __str__(self):
        return 'PlatForm: Lx %s Rx %s H %s' % (self.lx, self.rx, self.h)


class Solution(object):
    def help_jimmy(self, platforms, start, maxHeight):
        """
        :type triangle: List[PlatForm]
        :type start: Tuple
        :type maxHeight: int
        :rtype: int
        """
        n = len(platforms)
        Infinite = 1 << 31
        leftMinTime = [0] * (n + 1)
        rightMinTime = [0] * (n + 1)
        platforms.insert(0, PlatForm(start[0], start[0], start[1]))
        # 对所有平台按高度大小进行降序排序
        platforms = sorted(platforms, key=lambda p: p.h, reverse=True)

        for i in range(n, -1, -1):
            j = i + 1
            while j <= n:  # 寻找i的左端下方的平板
                if platforms[j].lx <= platforms[i].lx <= platforms[j].rx: break
                j += 1
            if j > n:
                leftMinTime[i] = Infinite if platforms[i].h > maxHeight else platforms[i].h
            else:
                _h = platforms[i].h - platforms[j].h
                if _h > maxHeight:
                    leftMinTime[i] = Infinite
                else:
                    leftMinTime[i] = min(leftMinTime[j] + platforms[i].lx - platforms[j].lx,
                                         rightMinTime[j] + platforms[j].rx - platforms[i].lx) + _h
            j = i + 1
            while j <= n:  # 寻找i的右端下方的平板
                if platforms[j].lx <= platforms[i].rx <= platforms[j].rx: break
                j += 1
            if j > n:
                rightMinTime[i] = Infinite if platforms[i].h > maxHeight else platforms[i].h
            else:
                _h = platforms[i].h - platforms[j].h
                if _h > maxHeight:
                    rightMinTime[i] = Infinite
                else:
                    rightMinTime[i] = min(leftMinTime[j] + platforms[i].rx - platforms[j].lx,
                                          rightMinTime[j] + platforms[j].rx - platforms[i].rx) + _h

        if leftMinTime[0] >= Infinite: return -1
        return leftMinTime[0]


if __name__ == '__main__':
    solution = Solution()
    platforms = [
        PlatForm(0, 10, 8),
        PlatForm(0, 10, 13),
        PlatForm(4, 14, 3)
    ]
    print(solution.help_jimmy(platforms, start=(8, 17), maxHeight=20))
