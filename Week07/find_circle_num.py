from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        """
        并查集解法：将属于同一个朋友圈的所有成员加入同一个并查集，统计最后的并查集的数量即可
        """

        # 并查集定义
        p = [i for i in range(len(M))]

        def find(a):
            if p[a] != a:
                # 路径压缩
                p[a] = find(p[a])
            return p[a]

        def union(a, b):
            p[find(b)] = find(a)
            return find(b)

        # 遍历矩阵，将属于朋友关系的两个成员所属的并查集合并
        for a in range(len(M)):
            for b in range(a):
                if M[a][b]:
                    union(a, b)

        # 执行路径压缩，使得属于同一个并查集的元素对应的 p 数组上的值保持一致
        for i in range(len(M)):
            find(i)

        return len(set(p))