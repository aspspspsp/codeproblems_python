import heapq

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._heap = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._stack.append(x)
        heapq.heappush(self._heap, x)

    def pop(self):
        """
        :rtype: None
        """
        x = self._stack.pop()
        if x == self.getMin():
            heapq.heappop(self._heap)

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._heap[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
