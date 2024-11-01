class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda item: item[0])
        prev = intervals[0]
        overlaps = []

        for interval in intervals[1:]:
            if prev[1] > interval[0]:
                prev[1] = max(prev[1], interval[1])

            elif prev[1] == interval[0]:
                prev[1] = interval[1]

            else:
                overlaps.append(prev)
                prev = interval

        overlaps.append(prev)

        return overlaps

        