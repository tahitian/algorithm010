from typing import List, Union


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Union[TreeNode, None]:
        """
        递归解法：从前序列表中获取第一个元素，该元素是根结点
                然后在中序序列中找到该元素，元素左侧的 n 个元素构成了根结点的左子树
                前序序列根结点元素之后的 n 个元素也构成了左子树，在两个左子树的序列上递归
                同理在两个右子树的序列上递归
        时间复杂度：每一轮递归的时间复杂度在于 inorder.index()，也就是递归的子树序列的长度
                从树形图来看，每一层的递归的时间复杂度之和是该层分散出的所有子树序列的长度之和，也就是总序列的长度 O(n)
                一共有平均 O(logn) 层递归，所以总的时间复杂度是 O(nlogn)
        空间复杂度：每一层递归大概使用切片复制一半的序列上层序列长度，因此总的空间复杂度是 O(n)
                改用 start、end 而不是使用切片来获取子树序列的话，空间复杂度可以降为 O(logn)
        """
        if not preorder:
            return None
        root_val = preorder[0]
        i = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root