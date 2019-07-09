# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self._maxDepth(root, 0)

    def _maxDepth(self, root, depth):
        if not root:
            return depth;

        l = self._maxDepth(root.left, depth + 1)
        r = self._maxDepth(root.right, depth + 1)

        if l >= r:
            return l

        return r
