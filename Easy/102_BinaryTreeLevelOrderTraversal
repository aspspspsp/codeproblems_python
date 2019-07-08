# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = [[]]
        self._levelOrder(root, 0, res)

        return res

    def _levelOrder(self, root, cur_level, res):
        if root is None:
            return

        if cur_level >= len(res):
            res.append([])

        res[cur_level].append(root.val)

        self._levelOrder(root.left, cur_level + 1, res)
        self._levelOrder(root.right, cur_level + 1, res)
