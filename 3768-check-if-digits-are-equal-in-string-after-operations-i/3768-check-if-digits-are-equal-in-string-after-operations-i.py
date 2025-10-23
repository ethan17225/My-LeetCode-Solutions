class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            n = len(s)
            i = 0
            sub = ""
            while i + 1 < n:
                sub += str((int(s[i]) + int(s[i+1])) % 10)
                i += 1

            s = sub

        return True if s[0] == s[1] else False