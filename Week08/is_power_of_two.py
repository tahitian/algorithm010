class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        x & (x-1) 的作用是将二进制数的最后一个非零位置零
        2 的整数次幂的二进制表示中有且只有一位是 1，所以执行 x & (x-1) 的结果是 0
        """
        return n != 0 and n & (n-1) == 0