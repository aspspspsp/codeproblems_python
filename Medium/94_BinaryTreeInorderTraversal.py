# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self._inorderTraversal(root, res)

        return res

    def _inorderTraversal(self, root, res):

        if root.left:
            self._inorderTraversal(root.left, res)

        res.append(root.val)

        if root.right:
            self._inorderTraversal(root.right, res)
