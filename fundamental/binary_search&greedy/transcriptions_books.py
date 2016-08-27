#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
誊抄书籍:
有 m 本书需要誊抄, 每本书的页数分别是 (p1 , p2 , …, pm )
• 有 k (k <= m) 个抄写员负责誊抄这些书籍任务
• 将这些书分成 k 份, 每本书必须只分给一个抄写员且每个抄写员至少分到一本
• 要求每个抄写员分到的书的编号是连续的, 即存在一个连续升序数列 0=b 0 ＜b 1 ＜b 2 ＜…＜b k-1 ＜b k =m
  这样, 第 i-1 号抄写员得到的书稿是从 b i-1 +1 到第 b i 本书
复制工作是同时开始进行的且每个抄写员复制的速度都是一样的
复制完所有书稿所需时间取决于分配得到 最多工作 的那个抄写员的复制时间
现要求分到页数最多的抄写员需要抄写的页数尽可能少,求最优的分配方式
"""


class Solution(object):
    def transcriptions_books(self, books, k):
        """
        :type books: List[int]
        :type k: int
        :rtype: void
        """

        def check(pages):
            mass = currPages = 0
            for i in range(m - 1, -1, -1):
                if books[i] + currPages > pages:
                    mass += 1
                    currPages = books[i]
                else:
                    currPages += books[i]
            if currPages > 0: mass += 1
            return mass <= k

        def build_result(bookNo, staff, currPages, pages):
            if bookNo < 0: return
            separator = False
            if bookNo == staff - 1 or currPages + books[bookNo] > pages:
                build_result(bookNo - 1, staff - 1, books[bookNo], pages)
                separator = True
            else:
                build_result(bookNo - 1, staff, currPages + books[bookNo], pages)
            if bookNo > 0: self.result += ' '
            self.result += str(books[bookNo])
            if separator: self.result += ' /'

        m = len(books)
        if m < k: return
        left = right = 0
        for b in books:
            if b > left: left = b
            right += b
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        pages = left
        self.result = ''
        build_result(m - 1, k - 1, 0, pages)
        print('Max Pages: %d\t\t%s' % (pages, self.result))


if __name__ == '__main__':
    solution = Solution()
    books = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    solution.transcriptions_books(books, 3)
    solution.transcriptions_books([100, 100, 100, 100, 100], 4)
