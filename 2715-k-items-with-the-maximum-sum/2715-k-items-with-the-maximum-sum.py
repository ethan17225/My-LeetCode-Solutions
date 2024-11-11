class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        max_sum = 0

        for i in range(k):
            if numOnes > 0:
                max_sum += 1
                numOnes -= 1
            elif numZeros > 0:
                numZeros -= 1
            else:
                max_sum -=1
                numZeros -= 1

        return max_sum