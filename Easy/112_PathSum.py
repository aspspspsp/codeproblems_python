# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        return self._hasPathSum(root, sum)

    def _hasPathSum(self, root, sum):
        if root.left is None and root.right is None:
            if sum == root.val:
                return True
            return False

        sum -= root.val

        isVaild = False
        if root.left:
            isVaild = isVaild or self._hasPathSum(root.left, sum)

            # 早停止
            if isVaild:
                return True

        if root.right:
            isVaild = isVaild or self._hasPathSum(root.right, sum)

        return isVaild
