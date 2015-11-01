# coding: utf-8
__author__ = 'devin'


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = dict()
        for val in nums:
            if val in d.keys():
                return True
            d[val] = 1
        return False

    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        data = set(nums)
        if len(data)-len(nums) < 0:
            return True
        return False

    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        data_len = len(nums)
        for i in range(data_len):
            for j in range(i+1,data_len):
                if nums[i] == nums[j]:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    dd = [1, 2, 3]
    print s.containsDuplicate2(dd)

