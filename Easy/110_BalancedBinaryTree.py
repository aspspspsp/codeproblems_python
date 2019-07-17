# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 二叉平衡樹就是一個節點的左右子樹的深度差不超過1，而左右子樹也都是二叉平衡樹

        return self._isBalanced(root)

    def _isBalanced(self, root):
        # 歷遍至根節點以下時則這棵樹歷遍完畢
        if root is None:
            return True

        # 取得兩個子樹的高度
        l = self.getDepth(root.left, 1)
        r = self.getDepth(root.right, 1)

        # 若高度差超過1則為False
        if abs(l - r) > 1:
            return False

        # 兩邊子樹分別做下去
        return self._isBalanced(root.left) and self._isBalanced(root.right)

    def getDepth(self, root, cur_depth):
        if root is None:
            return cur_depth - 1

        l = self.getDepth(root.left, cur_depth + 1)
        r = self.getDepth(root.right, cur_depth + 1)

        return max(l, r)
