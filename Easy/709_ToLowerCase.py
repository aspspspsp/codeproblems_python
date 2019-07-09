class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """

        dic = {"A": 'a', "B": 'b', "C": 'c',
               "D": 'd', "E": 'e', "F": 'f',
               "G": 'g', "H": 'h', "I": 'i',
               "J": 'j', "K": 'k', "L": 'l',
               "M": 'm', "N": 'n', "O": 'o',
               "P": 'p', "Q": 'q', "R": 'r',
               "S": 's', "T": 't', "U": 'u',
               "V": 'v', "W": 'w', "X": 'x',
               "Y": 'y', "Z": 'z'}
        res = ''
        for s in str:
            if s in dic.keys():
                s = dic[s]
            res += s
        return res
