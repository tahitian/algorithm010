from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        最优子问题定义：dp[i][j] 表示以 matrix[i][j] 定点为右下角的正方形的最大变长
        状态转移方程：dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
        其它：
            边界条件判断优化：在原矩形的左边和上边分别加上一列 0 和一行 0
            空间优化：二维的缓存变成一维的缓存
        时间复杂度：O(m*n)
        空间复杂度：O(n)
        """
        if not matrix or len(matrix[0]) == 0:
            return 0

        height, width = len(matrix), len(matrix[0])
        max_side = 0
        dp = [0] * (width + 1)

        for i in range(height):
            northwest = 0
            for j in range(width):
                next_northwest = dp[j + 1]
                if matrix[i][j] == "1":
                    dp[j + 1] = min(dp[j], dp[j + 1], northwest) + 1
                    max_side = max(max_side, dp[j + 1])
                northwest = next_northwest

        return max_side * max_side