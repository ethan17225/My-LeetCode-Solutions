class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True

        while n != 1:
            temp = n / 3
            n //= 3

            if n != temp:
                return False

        return True