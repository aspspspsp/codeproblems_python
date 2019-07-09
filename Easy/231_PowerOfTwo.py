import math


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        if n == (2 ** round(math.log(n, 2), 1)):
            return True

        return False
