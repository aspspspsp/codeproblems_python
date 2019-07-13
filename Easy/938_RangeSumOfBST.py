# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        self._sum = 0

        self._rangeSumBST(root, L, R)

        return self._sum

    def _rangeSumBST(self, root, L, R):
        if L <= root.val <= R:
            self._sum += root.val

        if root.left:
            if root.left > L:
                self._rangeSumBST(root.left, L, R)

        if root.right:
            if root.right > R:
                self._rangeSumBST(root.right, L, R)
