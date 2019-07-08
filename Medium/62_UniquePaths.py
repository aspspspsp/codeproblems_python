class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        martix = [[None] * m] * n

        for i in range(0, n):
            for j in range(0, m):
                # 原點
                if i == 0 and j == 0:
                    martix[i][j] = 1
                # y軸
                elif i == 0:
                    martix[i][j] = martix[i][j - 1]
                # x 軸
                elif j == 0:
                    martix[i][j] = martix[i - 1][j]
                else:
                    martix[i][j] = martix[i - 1][j] + martix[i][j - 1]

        return martix[n - 1][m - 1]
