class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pairs = {s[0]: t[0]}

        for i in range(1, len(s)):
            if s[i] not in pairs:
                pairs[s[i]] = t[i]
                values = pairs.values()
                if len(values) > len(set(values)):
                    return False

            else:
                if pairs[s[i]] != t[i]:
                    return False 

        return True

    