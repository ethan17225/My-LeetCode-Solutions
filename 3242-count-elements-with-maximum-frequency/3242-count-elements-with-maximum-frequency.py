from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        max_freq = 0
        total_freq = 0

        for num in nums:
            f = freq[num] + 1
            freq[num] = f

            if max_freq < f:
                max_freq = f

        for f in freq.values():
            if max_freq == f:
                total_freq += f

        return total_freq

        

        