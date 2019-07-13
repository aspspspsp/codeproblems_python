class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        nums| 2 -1 -5  2  3 -6  2  6 -3
      =================================
      curSum| 2  1  0  2  5  0  2  8  5
        '''

        maximum = -2147483647
        curSum = 0

        # 貪心法，一直將元素放進背包裡，一但揹包裡的總值小於0，則reset背包
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num

            maximum = max(curSum, maximum)

        return maximum
