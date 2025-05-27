class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        if m > n:
            return sum([x for x in range(1, n+1)])

        if m == n:
            return sum([x for x in range(1, n)]) - n

        arr = [x for x in range(1, n+1)]
        total = sum(arr)
        non_divisible_arr_total = sum([x for x in arr if x % m != 0])

        return non_divisible_arr_total - (total - non_divisible_arr_total)

    

        