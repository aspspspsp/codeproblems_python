"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []

        self._levelOrder(root, 0, res)
        return res

    def _levelOrder(self, root, cur_level, res):
        if root is None:
            return

        if cur_level >= len(res):
            res.append([])

        res[cur_level].append(root.val)

        for child in root.children:
            self._levelOrder(child, cur_level + 1, res)
