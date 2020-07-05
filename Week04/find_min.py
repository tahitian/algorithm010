from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        使用二分法，比较中间值和最右值：
            当中间值小于最右值的时候，最小值在左边区间
            当中间值大于最右值的时候，最小值在右边区间
        其它细节：
            为什么是比较最右值而不是最左值：
                因为当存在没有反转的情况的时候，如果中间值大于最左值，这时候无法判断最小值是在左区间还是在右区间
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]