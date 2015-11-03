# coding: utf-8
__author__ = 'devin'

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        counter = 0
        ret_num = 0
        for i in range(nums_len):
            if counter == 0:
                ret_num = nums[i]
                counter += 1
            else:
                if ret_num == nums[i]:
                    counter += 1
                else:
                    counter -= 1
        return ret_num


if __name__ == '__main__':
    s = Solution()
    nums = [3, 3, 3, 4]
    print s.majorityElement(nums)