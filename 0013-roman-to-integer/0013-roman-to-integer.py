class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        slen = len(s)
        result = 0
        a = 0
        b = 1
        while b < slen:
            if roman[s[a]] >= roman[s[b]]:
                result += roman[s[a]]
                a += 1
                b+=1
            else:
                result += roman[s[b]] - roman[s[a]]
                a += 2
                b += 2

        while a < slen:
            result += roman[s[a]]
            a += 1

        return result 