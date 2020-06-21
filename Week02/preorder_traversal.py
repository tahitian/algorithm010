from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 颜色标记法的变形，对于当前节点不需要标记，直接存到结果列表中即可
        res, stack = [], [root] if root else []
        while stack:
            i = stack.pop()
            res.append(i.val)
            stack.extend([j for j in [i.right, i.left] if j is not None])
        return res

    def preorderTraversal_02(self, root: TreeNode) -> List[int]:
        # 手动实现递归栈
        node, stack, res = root, [], []
        while node or stack:
            if node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop().right
        return res

    def preorderTraversal_03(self, root: TreeNode) -> List[int]:
        # 递归法
        return [] if not root else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)