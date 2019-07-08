# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self._levelOrderBottom(root, 0, res)
        res.reverse()
        return res

    def _levelOrderBottom(self, root, cur_level, res):
        if root is None:
            return

        if cur_level >= len(res):
            res.append([])

        res[cur_level].append(root.val)

        self._levelOrderBottom(root.left, cur_level + 1, res)
        self._levelOrderBottom(root.right, cur_level + 1, res)
