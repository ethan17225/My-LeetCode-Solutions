class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        temp = nums[0]
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                max_sum = max(max_sum, temp)
                temp = 0

            temp += nums[i]

        return max(max_sum, temp)
            
