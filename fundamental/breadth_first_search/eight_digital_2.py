#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
八数码:
    有一个3*3的棋盘，其中有0-8共9个数字，0表示空格，其他的数字可以和0交换位置。求由初始状态到达目标状态的步数最少的解。
双向广搜：加快搜索，提高效率。
"""


class Solution(object):
    def eight_digital(self, src, target):
        """
        :type src: str
        :type target: str
        :rtype: void
        """

        class Node(object):
            def __init__(self, num, father=None, move=''):
                self.num = num
                self.father = father  # 父节点在队列中的下标位置
                self.move = move  # 父节点的移动步骤

        # 给定排列s求序号
        def GetPermutationNumByStr(s):
            num, n = 0, len(s)
            permutation = list(map(int, list(s)))
            used = [False] * n
            for i in range(n):
                c = 0
                for j in range(permutation[i]):
                    if not used[j]: c += 1
                num += c * factorial[n - i - 1]
                used[permutation[i]] = True
            return num

        # 给定序号num求排列
        def GetPermutationStrByNum(num, n):
            s = ''
            used = [False] * n
            for i in range(n):
                j = 0
                while j < n:
                    if not used[j]:
                        if factorial[n - i - 1] >= num + 1: break
                        num -= factorial[n - i - 1]
                    j += 1
                s += str(j)
                used[j] = True
            return s

        # 求从原先序号经过 move 移动操作后得到的新序号。若移动不可行则返回-1
        def GetNewPermutationNum(prevNum, move):
            prevS = GetPermutationStrByNum(prevNum, self.N)
            idx = prevS.index('0')
            newLst = list(prevS)
            if move == 'u':
                if idx < 3: return -1
                newLst[idx], newLst[idx - 3] = newLst[idx - 3], '0'
            elif move == 'r':
                if idx % 3 == 2: return -1
                newLst[idx], newLst[idx + 1] = newLst[idx + 1], '0'
            elif move == 'd':
                if idx > 5: return -1
                newLst[idx], newLst[idx + 3] = newLst[idx + 3], '0'
            elif move == 'l':
                if idx % 3 == 0: return -1
                newLst[idx], newLst[idx - 1] = newLst[idx - 1], '0'
            return GetPermutationNumByStr(''.join(newLst))

        # 判断排列的奇偶性：True为奇排列  False为偶排列
        def GetPermutationType(s):
            _sum = 0
            for i in range(1, len(s)):
                if s[i] == '0': continue
                for j in range(i):
                    if s[j] < s[i] and s[j] != '0': _sum += 1
            return _sum % 2 != 0

        def oppositeDir(move):
            if move == 'u':
                return 'd'
            elif move == 'r':
                return 'l'
            elif move == 'd':
                return 'u'
            elif move == 'l':
                return 'r'

        def dbfs():
            srcNum, targetNum = GetPermutationNumByStr(src), GetPermutationNumByStr(target)
            visited[0][srcNum] = True
            visited[1][targetNum] = True
            queue[0].append(Node(srcNum))
            queue[1].append(Node(targetNum))
            while self.qHead[0] < self.qTail[0] and self.qHead[1] < self.qTail[1]:
                qNo = 0 if self.qTail[0] - self.qHead[0] <= self.qTail[1] - self.qHead[1] else 1
                num = queue[qNo][self.qHead[qNo]].num
                if visited[1 - qNo][num]:  # 出来的元素在另一队列中遍历过
                    self.matchingInfo = (qNo, num)
                    return True
                else:
                    for move in ('u', 'r', 'd', 'l'):
                        newNum = GetNewPermutationNum(num, move)
                        if newNum == -1: continue
                        if visited[qNo][newNum]: continue
                        visited[qNo][newNum] = True
                        queue[qNo].append(Node(newNum, self.qHead[qNo], move))
                        self.qTail[qNo] += 1
                    self.qHead[qNo] += 1
            return False

        self.N = len(src)
        factorial = [1] * (self.N + 1)
        for i in range(1, self.N + 1): factorial[i] = factorial[i - 1] * i
        visited = [[False] * factorial[self.N], [False] * factorial[self.N]]
        queue = [[], []]
        self.qHead, self.qTail = [0, 0], [1, 1]
        # 八数码问题有解性的判定: 排列有奇排列和偶排列两类，从奇排列不能转化成偶排列或相反。
        if GetPermutationType(src) != GetPermutationType(target):
            print('Unsolvable.')
            return
        self.matchingInfo = None
        if dbfs():
            result = []
            qNo, num = self.matchingInfo
            if qNo == 0:
                node = queue[qNo][self.qHead[qNo]]
            else:
                i = 0
                while i <= self.qTail[1 - qNo]:
                    if queue[1 - qNo][i].num == num: break
                    i += 1
                node = queue[1 - qNo][i]
            while node.father is not None:
                result.append(node.move)
                node = queue[0][node.father]
            result.reverse()
            if qNo == 0:
                i = 0
                while i <= self.qTail[1 - qNo]:
                    if queue[1 - qNo][i].num == num: break
                    i += 1
                node = queue[1 - qNo][i]
            else:
                node = queue[qNo][self.qHead[qNo]]
            while node.father is not None:
                result.append(oppositeDir(node.move))
                node = queue[1][node.father]
            print(''.join(result))
        else:
            print('Unsolvable.')


if __name__ == '__main__':
    solution = Solution()
    solution.eight_digital('234150768', '123456780')
    solution.eight_digital('871526340', '123456780')
    solution.eight_digital('871625340', '123456780')
    solution.eight_digital('012345678', '123456780')
