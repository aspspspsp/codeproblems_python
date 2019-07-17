from collections import deque


class LRUCache(object):
    '''
    LRU像是管理固定大小的衣櫥一樣
    穿衣服時：
    把裡面的衣服拿出來穿上，然後不穿的時候將那件衣服放在最前面
    放新衣服時：
        如果沒有一樣的衣服：
        每次都把最新的衣服放在最前面，而每次放衣服的時候都會檢查衣櫥
        是否已經滿了，滿了則把最後面的衣服丟掉
        如果有一樣的衣服：
        則將這件衣服放到最前面
    '''
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hash_map = dict() # 定義hash map存值
        self.queue = deque() # 定義雙向隊列存key

    def is_full(self):
        return len(self.queue) == self.capacity

    def _move_to_top(self, key):
        self.queue.remove(key)
        self.queue.appendleft(key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash_map:
            return -1

        # 把這個key移動到最前面
        self._move_to_top(key)

        return self.hash_map[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 如果沒有一樣的key
        if key not in self.hash_map:
            # 如果deque滿了，則把最後的值排出
            if self.is_full():
                pop_key = self.queue.pop()
                self.hash_map.pop(pop_key)
            # 放入最新值
            self.queue.appendleft(key)
            self.hash_map[key] = value
        # 若有一樣的key
        else:
            self.hash_map[key] = value
            # 把這個key放到最前面
            self._move_to_top(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
