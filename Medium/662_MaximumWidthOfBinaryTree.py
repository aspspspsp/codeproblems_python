# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        tmp = []
        self._widthOfBinaryTree(root, 1, tmp, 0)

        res = 0
        for t in tmp:
            l = t[0]
            r = t[1]

            res = max(r - l + 1, res)

        return res

    def _widthOfBinaryTree(self, root, i, tmp, cur_lv):
        if not root:
            return

        if cur_lv >= len(tmp):
            tmp.append([i, i])

        if i < tmp[cur_lv][0]:
            tmp[cur_lv][0] = i

        if i > tmp[cur_lv][1]:
            tmp[cur_lv][1] = i

        if root.left:
            self._widthOfBinaryTree(root.left, i * 2, tmp, cur_lv + 1)
        if root.right:
            self._widthOfBinaryTree(root.right, i * 2 + 1, tmp, cur_lv + 1)
