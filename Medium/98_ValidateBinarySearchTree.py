# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self._isValidBST(root, -2 ** 32, 2 ** 32)

    def _isValidBST(self, root, curMin, curMax):
        '''
        檢查當前節點值是否在當前最大與最小的範圍內
        若不是則返回False
        左子樹範圍 當前最小～當前值
        右子樹範圍 當前值～當前最大
        例如：
                 9   範圍：-無限~無限
                / \
範圍：-無限~9    7   11  範圍：9~無限
              / \  / \
範圍：-無限~7  4  8 10  12  範圍：11~無限
           範圍7~9 範圍：9~11
        '''
        if root is None:
            return True

        if root.val >= curMax:
            return False

        if root.val <= curMin:
            return False

        lValid = self._isValidBST(root.left, curMin, root.val)
        rValid = self._isValidBST(root.right, root.val, curMax)

        return lValid and rValid
