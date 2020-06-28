from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法：通过枚举不同的首元素来实现分支，选择了第 i 位作为首元素后，交换第 0 位和第 i 位，然后在除了首元素外的剩余序列中递归
        时间复杂度：一共有 n! 次枚举，每次枚举的结束都执行一次时间复杂度为 O(n) 的拷贝，所以总时间复杂度是 O(n*n!)
        空间复杂度：中间只是用了临时变量 start，个数是递归的深度，所以空间复杂度是 O(n)
        """
        n, result = len(nums), []
        def helper(start=0):
            if start == n:
                result.append(nums[:])
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                helper(start+1)
                nums[start], nums[i] = nums[i], nums[start]
        helper()
        return result
