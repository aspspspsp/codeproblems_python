# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
  :type root1: TreeNode
  :type root2: TreeNode
  :rtype: bool
  """
        root1_seq = []
        self.get_left_sequence(root1, root1_seq)

        root2_seq = []
        self.get_left_sequence(root2, root2_seq)

        if len(root1_seq) != len(root2_seq):
            return False

        for i in range(0, len(root1_seq)):
            if root1_seq[i] != root2_seq[i]:
                return False
        return True

    def get_left_sequence(self, root, seq):
        if root.left is None and root.right is None:
            seq.append(root.val)

        if root.left:
            self.get_left_sequence(root.left, seq)

        if root.right:
            self.get_left_sequence(root.right, seq)
