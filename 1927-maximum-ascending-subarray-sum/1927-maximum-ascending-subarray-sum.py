class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        temp = 0
        n = len(nums)
        i = 0

        if n == 1:
            return nums[0]

        while i < n:
            if i == n-1:
                if nums[i] > nums[i-1]:
                    temp += nums[i]

                return max_sum if temp <= max_sum else temp

            if nums[i] >= nums[i+1]:
                temp += nums[i]
                i += 1

                if temp > max_sum:
                    max_sum = temp

                temp = 0    

            else:
                temp += nums[i]
                i += 1

        return max_sum
