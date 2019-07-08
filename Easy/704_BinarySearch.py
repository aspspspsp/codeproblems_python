class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self._binarySearch(0, len(nums) - 1, nums, target)

    def _binarySearch(self, i, j, nums, target):
        p = int((i + j) / 2)
        if target == nums[p]:
            return p

        if i > j:
            return -1

        if nums[p] > target:
            return self._binarySearch(i, p - 1, nums, target)
        elif nums[p] < target:
            return self._binarySearch(p + 1, j, nums, target)
