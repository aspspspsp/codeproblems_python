# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self._pruneTree(root)

    #     1          1.  拜訪到最下面的葉子結點
    #    / \         2.  若葉子結點值為0，則回傳None(廢棄該節點)，若非為0則回傳自己
    #   1   0        3.  到上一節點(a)將左右子節點連接起來
    #      / \       3.1 若a左右子節點任一非為空則直接回傳，重複步驟3
    #     0   1      3.2 若a左右子節點為空則視為該點為子節點，重複2
    #    / \         4.  若做到根節點則結束
    #   0   0

    def _pruneTree(self, root):
        if root is None:
            return None

        left = root.left
        right = root.right

        if left is None and right is None:
            if root.val == 0:
                return None
            return root

        root.left = self._pruneTree(root.left)
        root.right = self._pruneTree(root.right)

        # 若為葉子結點，且值為0，則廢棄其節點
        if root.left is None and root.right is None:
            if root.val == 0:
                return None

        return root
