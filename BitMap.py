# coding: utf-8
__author__ = 'devin'
from array import *
from struct import *
from os import stat


class BitMap(object):
    def __init__(self):
        self._bitmap = array('L')  # unsigned long (4 bytes)

    def init(self, n):
        array_size = 1 + n/32
        i = 1
        while i <= array_size:
            self._bitmap.append(0)
            i += 1

    def set(self, num):
        self._bitmap[num >> 32] |= (1 << (num & 0x1f))

    def clr(self, num):
        self._bitmap[num >> 32] &= ~(1 << (num & 0x1f))

    def test(self, num):
        return not ((self._bitmap[num >> 32] & (1 << (num & 0x1f))) == 0)

    def save(self, filename='result.txt'):
        with open(filename, 'wb') as fw:
            self._bitmap.write(fw)

    def read(self, filename='result.txt'):
        with open(filename, 'rb') as fr:
            file_info = stat(filename)
            self._bitmap.read(fr, file_info.st_size/calcsize('L'))

if __name__ == '__main__':
    # nums = [1, 2, 4, 5, 6, 7, 30, 31]
    # bitMap = BitMap()
    # bitMap.init(31)
    # for i in nums:
    #     bitMap.set(i)
    # for i in range(32):
    #     if bitMap.test(i):
    #         print i, "True"
    # bitMap.save()


    # bitMap = BitMap()
    # bitMap.read()
    # bitMap.save('o.txt')
    # print bitMap.test(3)


