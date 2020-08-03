import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)   # 获取之后调整元素位置
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)   # 如果关键字已经存在，调整该元素位置
        self.dic[key] = value
        if len(self.dic) > self.capacity:   # 如果超过了容量限制，则删除最旧元素
            self.dic.popitem(last=False)