class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        number = int("".join([str(num) for num in digits]))
        number += 1
        return [int(num) for num in str(number)]