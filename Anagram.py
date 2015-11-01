# coding:utf-8
__author__ = 'devin'

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len = len(s)
        t_len = len(t)
        if t_len != s_len:
            return False
        for i in range(s_len):
            if s[i] != t[t_len-i-1]:
                return False
        return True

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str_s = "".join(sorted(s))
        str_t = "".join(sorted(t))
        if str_s == str_t:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print s.isAnagram("abc", "cba")
    print sorted("bca")
    print "acb" == "abc"
