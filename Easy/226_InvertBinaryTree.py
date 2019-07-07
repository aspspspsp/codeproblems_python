# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None

        self._invertTree(root)

        return root

    def _invertTree(self, root):
        if root is None:
            return root

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self._invertTree(root.left)
        self._invertTree(root.right)
