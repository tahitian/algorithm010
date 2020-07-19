from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        最优子问题：dp[i][j] 表示从左上角走到 maxtrix[i][j] 的最小路径长
        状态转移方程：dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]
        空间优化：直接在原二维数组上缓存中间结果
        时间复杂度：O(m*n)
        空间复杂度：O(1)
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[-1][-1]