from Libs.classes import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None:
            return None

        return self._constructMaximumBinaryTree(nums, 0, len(nums) - 1)
    # arr = [3,2,1,6,0,5]
    # 1. 從數組中找到最大值 ex:6
    # 2. 構建節點
    # 3. 構建左子樹，執行步驟1，傳入數組最大值的左邊元素ex:[3,2,1]，以及其左右邊界ex:l=0,r=2
    # 4. 構建右子樹，執行步驟1，傳入數組最大值的右邊元素ex:[0,5]，以及其左右邊界ex:l=4,r=5
    # 5. 若l=r表示這個子樹已經歷遍完畢，建立葉子節點並回傳該節點

    def _constructMaximumBinaryTree(self, nums, l, r):
        if l == r:
            _root = TreeNode(nums[l])
            return _root

        max_val = nums[l]
        max_ind = l
        for i in range(l, r + 1):
            if nums[i] > max_val:
                max_val = nums[i]
                max_ind = i

        left = None
        if max_ind - 1 >= l:
            left = self._constructMaximumBinaryTree(nums, l, max_ind - 1)

        right = None
        if max_ind + 1 <= r:
            right = self._constructMaximumBinaryTree(nums, max_ind + 1, r)

        root = TreeNode(max_val)
        root.left = left
        root.right = right

        return root
