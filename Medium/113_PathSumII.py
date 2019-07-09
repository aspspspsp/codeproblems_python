# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        self._pathSum(root, sum, [], res)
        return res

    def _pathSum(self, root, sum, tmp, res):
        # 若作法為葉節點下面才處理結果時，會多一個
        if root.left is None and root.right is None:
            sum = sum - root.val
            tmp.append(root.val)

            if sum == 0:
                res.append(tmp[:])
            return

        tmp.append(root.val)

        if root.left:
            self._pathSum(root.left, sum - root.val, tmp[:], res)
        if root.right:
            self._pathSum(root.right, sum - root.val, tmp[:], res)
