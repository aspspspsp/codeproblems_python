from Libs.classes import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self._mergedTrees(t1, t2)

    def _mergedTrees(self, t1, t2):
        if not t1 and not t2:
            return None

        root = None
        if t1 and not t2:
            root = TreeNode(t1.val)
            root.left = self._mergedTrees(t1.left, None)
            root.right = self._mergedTrees(t1.right, None)
        elif not t1 and t2:
            root = TreeNode(t2.val)
            root.left = self._mergedTrees(None, t2.left)
            root.right = self._mergedTrees(None, t2.right)
        else:
            root = TreeNode(t1.val + t2.val)
            root.left = self._mergedTrees(t1.left, t2.left)
            root.right = self._mergedTrees(t1.right, t2.right)

        return root
