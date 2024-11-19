class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        while i < n-1:
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
                i += 2
                continue

            i += 1

        nums = [num for num in nums if num != 0]

        n1 = len(nums)
        while n1 < n:
            nums.append(0)
            n1 += 1

        return nums


            