# coding: utf-8
__author__ = 'devin'

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs2(self, n):
        if n == 1:
            return 1
        if n==2:
            return 2
        f_1 = 1
        f_2 = 2
        i = 3
        result = 0
        while i <= n:
            result = f_1 + f_2
            f_1 = f_2
            f_2 = result
            i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(12)
