class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diff = 0
        chars = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1

                chars.append((s1[i], s2[i]))

            if diff > 2:
                return False

        if diff == 1 or len(chars) > 2:
            return False

        if chars[0][0] != chars[1][1] or chars[0][1] != chars[1][0]:
            return False

        return True
