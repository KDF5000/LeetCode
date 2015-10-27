# coding: utf-8
__author__ = 'devin'

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        i = 0
        zero_nums = 0
        while i < (nums_len - zero_nums):
            if nums[i] == 0:
                temp = nums[i]
                j = i+1
                while j < nums_len:
                    nums[j-1] = nums[j]
                    j += 1
                nums[j-1] = temp
                zero_nums += 1
            else:
                i += 1


if __name__ == '__main__':
    n = [0,1,0,3,12]
    s = Solution()
    s.moveZeroes(n)
    print n