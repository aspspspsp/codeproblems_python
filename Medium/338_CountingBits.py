import math
class Solution(object):
    ###############################
    # r n
    # 0 0    r[0] = 0
    # 1 1    r[1] = 1
    # =============================
    # 2 1|0  r[2] = r[2-2] = r[0] + 1 = 1
    # 3 1|1  r[3] = r[3-2] = r[1] + 1 = 2
    # =============================
    # 4 1|00 r[4] = r[4-4] = r[0] + 1 = 1
    # 5 1|01 r[5] = r[5-4] = r[1] + 1 = 2
    # 6 1|10 r[6] = r[6-4] = r[2] + 1 = 2
    # 7 1|11 r[7] = r[7-4] = r[3] + 1 = 3

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]

        res = [None] * (num + 1)

        res[0] = 0
        res[1] = 1

        a = 1

        for i in range(2, num + 1):
            p = int(math.pow(2, a))
            p1 = int(math.pow(2, a + 1))

            if i - p1 == 0:
                a += 1
                p = int(math.pow(2, a))

            res[i] = res[i - p] + 1

        return res
