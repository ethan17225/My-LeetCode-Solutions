class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return sorted(nums[0])

        result = set(nums[0]) & set(nums[1])
        if len(nums) == 2:
            return sorted(list(result))

        for i in range(2, len(nums)):
            result = result & set(nums[i])


        return sorted(list(result))
            
