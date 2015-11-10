# coding: utf-8
__author__ = 'devin'

class BackKnap(object):
    def __init__(self, weight=[], value=[]):
        if len(weight) != len(value):
            raise Exception("w,v must have same length!")

        self._weight = weight
        self._value = value
        self._n = len(weight)
        self._solution = []

    def boundF(self, cp, cw, k, M):
        """
        :param cp:
        :param cw:
        :param M:
        :return: maxValue
        """
        b = cp
        c = cw
        for i in range(k, self._n):
            c += self._weight[i]
            if c < M:
                b += self._value[i]
            else:
                return b + (1 - (c-M)/self._weight[i])*self._value[i]
        return b

    def backKnap(self, M):
        cw = 0
        cp = 0
        k = 0
        fp = -1
        Y = [0 for i in range(self._n)]
        X = [0 for i in range(self._n)]
        while True:
            while k < self._n and cw + self._weight[k] <= M:
                cw = cw + self._weight[k]
                cp = cp + self._value[k]
                Y[k] = 1
                k += 1
            if k > self._n - 1:
                fp = cp
                k = self._n -1
                X = Y[:]
                self._solution.append(X)
            else:
                Y[k] = 0
            while self.boundF(cp, cw, k+1, M) <= fp: # 必须是k+1,若是k第一次探索, fp=-1,boundF()永远不会小于等于-1,会死循环
                while k != -1 and Y[k] != 1:
                    k -= 1
                if k == -1:
                    return X
                Y[k] = 0
                cw -= self._weight[k]
                cp -= self._value[k]
            k += 1

    def getSolution(self):
        return self._solution


if __name__ == '__main__':
    w = [1, 11, 21, 23, 33, 43, 45, 55]
    v = [11, 21, 31, 33, 43, 53, 55, 65]
    s = BackKnap(w, v)
    res = s.backKnap(110)
    print res
    print s.getSolution()
