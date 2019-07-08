class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 對每一個數都進行抑或(XOR)運算，最後的結果即為答案
        result = nums[0]

        for i in range(1, len(nums)):
            result = result ^ nums[i]

        return result
