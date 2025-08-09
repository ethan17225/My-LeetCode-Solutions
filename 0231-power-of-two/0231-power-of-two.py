class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        if n == 0:
            return False

        while n != 1:
            temp = n // 2
            n /= 2
            if n != temp:
                return False

        return True

