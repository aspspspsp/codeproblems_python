class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(A), len(A[0])

        B = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                B[j][i] = A[i][j]

        return B
