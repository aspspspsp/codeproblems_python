class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        _set = set()
        for num in nums:
            if num in _set:
                return True
            _set.add(num)

        return False
