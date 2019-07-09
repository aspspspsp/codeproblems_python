"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        res.append(root.val)
        self._preorder(root, res)

        return res

    def _preorder(self, root, res):
        if not root:
            return

        for i in range(0, len(root.children)):
            res.append(root.children[i].val)
            self._preorder(root.children[i], res)
