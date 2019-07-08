class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        martix = [[0] * n] * m

        # 遇到障礙物該點為0，其他作法與UniquePath一樣
        for i in range(0, m):
            for j in range(0, n):
                # 遇障礙
                if obstacleGrid[i][j] == 1:
                    martix[i][j] = 0
                # 不遇障礙
                else:
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

        return martix[m - 1][n - 1]
