import math


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num <= 0:
            return False

        if int(4 ** math.ceil(math.log(num, 4))) == num:
            return True

        return False
