from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        """
        双指针解法
        """
        index = -1
        for i in nums:
            if index < 0 or nums[index] != i:
                index += 1
                nums[index] = i
        return index + 1

    # def removeDuplicates(self, nums: List[int]) -> int:
    #     """
    #     反向遍历，逐个删除重复项
    #     """
    #     for i in range(len(nums))[::-1]:
    #         if i-1 >= 0 and nums[i] == nums[i-1]:
    #             nums.pop(i)
    #
    #     return len(nums)
