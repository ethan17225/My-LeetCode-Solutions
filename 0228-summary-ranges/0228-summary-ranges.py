class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        result = []
        nums_length = len(nums)
        
        while i < nums_length:
            start = nums[i]
            while i < nums_length - 1 and nums[i] + 1 == nums[i+1]:
                i += 1

            if start != nums[i]:
                result.append(f"{start}->{nums[i]}")

            else:
                result.append(str(start))

            i += 1           

        return result