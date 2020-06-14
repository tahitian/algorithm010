from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        双指针解法
        level: 截止目前最低水位；因为积满水后整个柱状图只有一个山峰，两边都是单调的，在双指针夹逼的过程中，最低水位是单调递增的
        lower: 左右指针中高度较小的指针
        """
        level, sum, lower, left, right = 0, 0, 0, 0, len(height) - 1
        while left <= right:
            if height[left] <= height[right]:
                lower, left = left, left + 1
            else:
                lower, right = right, right - 1
            level = max(level, height[lower])
            sum += level - height[lower]
        return sum

    # def trap(self, height: List[int]) -> int:
    #     """
    #     单调栈解法
    #     """
    #     sum, stack = 0, []
    #     for i in range(len(height)):
    #         while stack and height[i] > height[stack[-1]]:
    #             bottom = stack.pop()
    #             if not stack:
    #                 break
    #             sum += (min(height[stack[-1]], height[i]) - height[bottom]) * (i - stack[-1] - 1)
    #         stack.append(i)
    #     return sum

