# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []

        self._preorderTraversal(root, res)

        return res

    def _preorderTraversal(self, root, res):
        if not root:
            return

        res.append(root.val)

        if root.left:
            self._preorderTraversal(root.left, res)

        if root.right:
            self._preorderTraversal(root.right, res)
