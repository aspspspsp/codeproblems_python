import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.arr = nums
        self.size = len(self.arr)

        # 使其堆化(由小到大)
        heapq.heapify(self.arr)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        heapq.heappush(self.arr, val)

        return self.arr[len(self.arr) - 1 - self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
