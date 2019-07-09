class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dic = {}

        majority_times = len(nums) / float(2)

        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1

            if dic[num] > majority_times:
                return num

        return -1
