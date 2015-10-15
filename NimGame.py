# coding:utf-8
__author__ = 'devin'


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 4:
            return True
        return not (self.canWinNim(n-1) and self.canWinNim(n-2) and self.canWinNim(n-3))

    def canWinNim2(self, n):
        if n < 4:
            return True

        a_1 = a_2 = a_3 = True
        res = False
        i = 4
        while i <= n:
            res = not (a_1 and a_2 and a_3)
            a_1 = a_2
            a_2 = a_3
            a_3 = res
            i += 1
        return res

    def canWinNim3(self, n):
        if n % 4 == 0:
            return False
        else:
            return True

if __name__ == "__main__":
    sl = Solution()
    print sl.canWinNim3(1348820612)


