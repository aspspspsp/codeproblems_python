# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        self._postorderTraversal(root, res)
        return res

    def _postorderTraversal(self, root, res):
        if not root:
            return None
        if root.left:
            self._postorderTraversal(root.left, res)
        if root.right:
            self._postorderTraversal(root.right, res)

        res.append(root.val)
