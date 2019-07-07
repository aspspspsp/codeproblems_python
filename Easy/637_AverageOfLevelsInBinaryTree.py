# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        if root is None:
            return []

        tmp = []

        self._averageOfLevels(root, 0, tmp)

        for i, t in enumerate(tmp):
            # 使用'float'避免無法得到小數點後面的位數
            t = float(sum(t)) / len(t)
            tmp[i] = t

        return tmp

    def _averageOfLevels(self, root, cur_level, tmp):
        if root is None:
            return

        if cur_level >= len(tmp):
            tmp.append([])

        tmp[cur_level].append(root.val)

        self._averageOfLevels(root.left, cur_level + 1, tmp)
        self._averageOfLevels(root.right, cur_level + 1, tmp)
