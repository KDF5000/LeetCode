# coding:utf-8
__author__ = 'devin'

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n > 0:
            bit = n & 0x1
            if bit == 1:
                total += 1
            n = n >> 1
        return total
