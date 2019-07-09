class Solution:
    def fib(self, N: int) -> int:
        fi = [None] * (N + 1)

        if N < 2:
            return N

        fi[0] = 0
        fi[1] = 1

        for i in range(2, N + 1):
            fi[i] = fi[i - 1] + fi[i - 2]

        return fi[N]
