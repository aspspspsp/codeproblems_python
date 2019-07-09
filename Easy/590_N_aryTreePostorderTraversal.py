"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        self._postorder(root, res)
        return res

    def _postorder(self, root, res):
        if root is None:
            return

        for child in root.children:
            self._postorder(child, res)
        res.append(root.val)
