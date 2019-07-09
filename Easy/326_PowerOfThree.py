import math


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 0:
            return False

        if n < 0:
            return False

        # 因為math.log於特定數字會有小數點的問題 ex: math.log(243) = 4.99999999，故不能
        # 直接使用float - int是否大於0的方法來判斷，只能依照冪次還原的方法來判斷，**運算符為冪次
        if n == int(3 ** math.ceil(math.log(n, 3))):
            return True

        return False
