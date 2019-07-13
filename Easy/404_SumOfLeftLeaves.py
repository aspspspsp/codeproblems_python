# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNod
        :rtype: int
        """
        if root is None:
            return 0

        tmp = []
        self._sumOfLeftLeaves(root, False, tmp)

        res = sum(tmp)

        return res

    def _sumOfLeftLeaves(self, root, isLeft, tmp):
        if root.left is None and root.right is None:
            if isLeft:
                tmp.append(root.val)
            return

        if root.left:
            self._sumOfLeftLeaves(root.left, True, tmp)
        if root.right:
            self._sumOfLeftLeaves(root.right, False, tmp)
