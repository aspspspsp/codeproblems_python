class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False

        if matrix[0] == []:
            return False

        n = len(matrix)
        m = len(matrix[0])

        for i in range(0, n):
            # 先確認target所在的橫排範圍(每一橫排開始歷遍)
            if matrix[i][0] == target:
                return True
            if matrix[i][m - 1] == target:
                return True
            if matrix[i][0] < target < matrix[i][m - 1]:
                # 若在該橫排之間，則開始一個個慢慢找
                for j in range(0, m):
                    if matrix[i][j] == target:
                        return True
                # 若該橫排範圍沒有，則可以早停止(因為過排序，左大右小，下大於上)
                return False
        # 都沒有
        return False
