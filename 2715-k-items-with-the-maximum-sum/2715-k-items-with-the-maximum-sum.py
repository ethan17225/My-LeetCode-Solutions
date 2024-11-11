class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        else:
            k -= (numOnes + numZeros)
            
            if k <= 0:
                return numOnes
            else:
                return numOnes - k