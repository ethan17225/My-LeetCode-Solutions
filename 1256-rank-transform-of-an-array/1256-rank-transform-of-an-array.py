class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = dict()
        n = len(arr)
        i = 1

        for num in sorted(set(arr)):
            rank[num] = i
            i += 1

        return [rank[num] for num in arr]
