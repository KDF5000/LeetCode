# coding: utf-8
__author__ = 'devin'

class Solution(object):
    def __init__(self):
        self._sub_s_word_break = dict()

    def joinWord(self, word, data=[]):
        if len(data) == 0:
            return [word]
        retData = []
        for d in data:
            word = word + " " + d
            retData.append(word)
        return retData

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if s in self._sub_s_word_break.keys():
            return self._sub_s_word_break[s]

        word = ''
        ret_list = []
        s_len = len(s)
        for i in range(s_len):
            word += s[i]
            if word in wordDict:
                sub_sentence = self.wordBreak(s[i+1:], wordDict)
                sentence = self.joinWord(word, sub_sentence)
                ret_list.extend(sentence)
        return ret_list


if __name__ == "__main__":
    s = Solution()
    str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    dic = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print s.wordBreak(str, dic)

    # print s.wordBreak("cutsanddog", ["cut", "cuts", "sand", "and", "dog"])








