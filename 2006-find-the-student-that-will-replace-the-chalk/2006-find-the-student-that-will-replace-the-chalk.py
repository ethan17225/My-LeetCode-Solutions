class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total = sum(chalk)

        remain = k % total

        if remain == 0:
            return 0

        else:
            for i in range(n):
                remain -= chalk[i]
                if remain == 0:
                    return i + 1
                elif remain < 0:
                    return i
            
        return ""
