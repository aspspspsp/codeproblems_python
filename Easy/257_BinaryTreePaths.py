# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        res = set()
        self._binaryTreePaths(root, "", res)

        return res

    def _binaryTreePaths(self, root, tmp, res):
        if not root.left and not root.right:
            tmp += str(root.val)
            res.add(tmp)
            return

        tmp += str(root.val) + '->'

        if root.left:
            self._binaryTreePaths(root.left, tmp, res)
        if root.right:
            self._binaryTreePaths(root.right, tmp, res)
