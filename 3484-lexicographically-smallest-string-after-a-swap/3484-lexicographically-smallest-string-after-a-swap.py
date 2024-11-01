class Solution:
    def getSmallestString(self, s: str) -> str:
        digits = [int(d) for d in s]

        i = 0

        while i < len(digits)-1:
            d1 = digits[i]
            d2 = digits[i+1]

            if d1%2 == d2%2 and d1 > d2:
                digits[i], digits[i+1] = d2, d1
                return "".join([str(d) for d in digits])
            
            i += 1

        return s