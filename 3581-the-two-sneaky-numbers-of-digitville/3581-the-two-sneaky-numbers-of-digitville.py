from collections import defaultdict

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        sneaky_nums = []

        for num in nums:
            freq[num] += 1

        for n, f in freq.items():
            if f == 1:
                continue

            sneaky_nums.append(n)

        return sneaky_nums