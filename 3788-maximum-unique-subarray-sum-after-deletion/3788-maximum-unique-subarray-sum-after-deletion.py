class Solution:
    def maxSum(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        maxSum = 0

        for num in uniqueNums:
            if num > 0:
                maxSum += num

        return maxSum if maxSum > 0 else max(uniqueNums)