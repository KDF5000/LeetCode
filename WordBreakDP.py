# coding: utf-8
__author__ = 'devin'

class Solution(object):
    def __init__(self):
        self._res = []
        self._dp = dict()  # 存储dp表
        self._midres = []

    def _trackWord(self, s, high):
        if high >= 0:
            for j in range(high+1):
                if self._dp[j][high-j]:
                    self._midres.append(s[j:high+1])
                    self._trackWord(s, j-1)
                    self._midres.pop()
        else:
            res = ''
            mid_res_len = len(self._midres)
            while mid_res_len > 0:
                res += self._midres[mid_res_len-1]
                if mid_res_len > 1:
                    res += " "
                mid_res_len -= 1
            self._res.append(res)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        s_len = len(s)
        for i in range(s_len):
            temp = []
            for j in range(i, s_len):
                if s[i:j+1] in wordDict:
                    # 如果字典中有这个单词
                    temp.append(True)
                else:
                    temp.append(False)
            self._dp[i] = temp
        # 判断从第一个字母开始是否有存在字典中的单词
        for i in range(len(self._dp[0])):
            if self._dp[0][i]:
                self._trackWord(s, s_len-1)
                break
        return self._res


if __name__ == "__main__":
    s = Solution()
    str = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    dic = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print s.wordBreak(str, dic)
    # print s.wordBreak("cutsanddog", ["cut", "cuts", "sand", "and", "dog"])

