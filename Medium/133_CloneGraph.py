"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # 記錄拜訪過的節點
        visited = set()

        # 紀錄圖
        # {
        #   1: [2,3,4] # node值(編號): node鄰居值(編號)
        # }
        dic = {}

        # 做DFS
        self.dfs(node, dic, visited)

        # 存儲結果圖
        res = {}

        # 建立所有複製的節點
        for key in dic.keys():
            node = Node(key, [])
            res[key] = node

        # 拜訪所有在複製圖的所有節點
        for key in res.keys():
            # 從dic找到該節點的所有鄰居的值(編號)，並將其與複製節點鄰居建立聯繫
            for n_val in dic[key]:
                res[key].neighbors.append(res[n_val])

        # 返回第一個節點
        return res[1]

    def dfs(self, node, dic, visited):
        # 遇拜訪過的則略過
        if node.val in visited:
            return

        # 將此節點的編號加入已拜訪清單
        visited.add(node.val)

        if node.val not in dic.keys():
            dic[node.val] = []

        # 對其鄰居進行拜訪
        for neighbor in node.neighbors:
            # 將鄰居的值(編號)放入鄰居列表，以便於與鄰居建立聯繫
            dic[node.val].append(neighbor.val)

            # 繼續拜訪下去
            self.dfs(neighbor, dic, visited)
