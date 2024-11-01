class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        nums_length = len(nums)
        left_sum = [0] * nums_length
        right_sum = [0] * nums_length

        i = 1
        while i < nums_length:
            j = -i - 1

            left_sum[i] = nums[i-1] + left_sum[i-1]
            right_sum[j] = nums[j+1] + right_sum[j+1]

            i += 1

        j = 0
        while j < nums_length:
            if left_sum[j] == right_sum[j]:
                return j

            j+=1

        return -1