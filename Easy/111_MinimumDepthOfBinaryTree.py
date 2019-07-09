# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self._minDepth(root, 0)

    def _minDepth(self, root, depth):
        if not root.left and not root.right:
            return depth + 1

        min_value = 9999
        if root.left:
            min_value = min(min_value, self._minDepth(root.left, depth + 1))

        if root.right:
            min_value = min(min_value, self._minDepth(root.right, depth + 1))

        return min_value
