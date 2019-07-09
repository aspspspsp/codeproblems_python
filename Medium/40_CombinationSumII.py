class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        # 因為在數組中有值相同的元素，例如：1，2，1，5，6，7，10，故先排序，以免答案重複
        candidates = sorted(candidates)

        self.dfs(0, candidates, target, [], res)
        return res

    def dfs(self, cur, candidates, target, tmp, res):
        if target == 0:
            res.append(tmp[:])

        if target < candidates[0]:
            return

        for i in range(cur, len(candidates)):
            # 早停止
            if target < candidates[i]:
                break

            # 這個判斷保證不重複，例如：1，1，2，5，6，7，10，歷遍到第二個1就會被跳過
            if i > cur and candidates[i] == candidates[i - 1]:
                continue

            # 將第i個元素加入答案中
            tmp.append(candidates[i])
            # 拜訪下一個
            self.dfs(i + 1, candidates, target - candidates[i], tmp[:], res)
            # 回復上一個狀態
            tmp.pop(-1)
