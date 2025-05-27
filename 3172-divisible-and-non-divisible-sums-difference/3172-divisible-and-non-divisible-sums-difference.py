class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        if m > n:
            return sum([x for x in range(1, n+1)])

        if m == n:
            return sum([x for x in range(1, n)]) - n

        total = non_divisible_total = 0
        i = 1

        while i <= n:
            total += i
            if i % m != 0:
                non_divisible_total += i

            i += 1

        return non_divisible_total - (total - non_divisible_total)

    

        