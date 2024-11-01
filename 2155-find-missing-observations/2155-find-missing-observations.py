class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:   
        m = len(rolls)
        remain_sum = mean*(m + n) - sum(rolls)

        if remain_sum < n*1 or remain_sum > n*6:
            return []

        remain_roll = [remain_sum // n] * n

        remain_sum = remain_sum%n

        i = 0
        while i < remain_sum:
            remain_roll[i] += 1
            i += 1

        return remain_roll