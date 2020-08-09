from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        状态定义：
            tails[i] 表示长度为 i 的增长子序列中的最小尾部值
        状态转移方程：
            当遍历到 nums[k] 时，
                如果存在 tails[i] > nums[k]：
                    将第一个满足 tails[i] > nums[k] 执行 tails[i] = nums[k]
                如果不存在 tails[i] > nums[k]：
                    tails[i+1] = nums[k]
        """
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1
                else:
                    j = m
            tails[i] = num
            if j == res:
                res += 1
        return res