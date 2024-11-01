
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closetNum = nums[0]

        for i in range(1, len(nums)):
            if abs(closetNum) > abs(nums[i]):
                closetNum = nums[i]

        if closetNum < 0 and abs(closetNum) in nums:
            return abs(closetNum)

        return closetNum

        

            