class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        n = len(s)
        m = len(words)
        i = 0
        J = 0

        while i < n:
            if J >= m:
                return False
        
            word = words[J]

            for char in word:
                if i >= n:
                    return False

                if s[i] != char:
                    return False

                i += 1

            J += 1

        return True

            