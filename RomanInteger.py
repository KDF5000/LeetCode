# coding: utf-8
__author__ = 'devin'

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_num_map = {"I": 1, "V": 5, "X": 10,  "L": 50, "C": 100, "M": 1000, "D": 500}
        s_len = len(s)
        num = 0
        for i in range(s_len):
            if s[i] not in str_num_map.keys():
                return 0
            if i < s_len-1 and str_num_map[s[i]] < str_num_map[s[i+1]]:
                num -= str_num_map[s[i]]
            else:
                num += str_num_map[s[i]]

        return num

if __name__ == '__main__':
    s = Solution()
    print s.romanToInt("MCMXCVI")


