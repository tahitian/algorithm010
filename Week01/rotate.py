from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        逐个交换元素，注意 k 和 len(nums) 存在最小公约数的情况
        通过将初始位置的值标记为 None 来判断是否返回了初始位置
        """
        if not nums or k % len(nums) == 0:
            return
        i, temp, nums[0], l = 0, nums[0], None, len(nums)
        for _ in range(l):
            j = (i + k) % l
            if nums[j] is None:
                nums[j], i, temp, nums[i] = temp, (j + 1) % l, nums[(j+1)%l], None
            else:
                nums[j], i, temp = temp, j, nums[j]
        nums[i] = temp

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     和上一种解法思路相同，但是用一个 start 变量来记录初始位置，使用了两层循环
    #     """
    #     l = len(nums)
    #     k %= l
    #     start, count = 0, 0
    #     while count < l:
    #         temp, nxt = nums[start], (start+k) % l
    #         while nxt != start:
    #             nums[nxt], temp, nxt = temp, nums[nxt], (nxt+k) % l
    #             count += 1
    #         nums[start], start = temp, start + 1
    #         count += 1

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     三次交换
    #     """
    #     k %= len(nums)
    #     nums[:] = nums[::-1]
    #     nums[:k], nums[k:] = nums[:k][::-1], nums[k:][::-1]