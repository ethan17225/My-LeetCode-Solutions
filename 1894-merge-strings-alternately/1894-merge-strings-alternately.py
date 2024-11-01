class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        result = []

        if len1 >= len2:
            i = 0
            while i < len2:
                result.append(word1[i])
                result.append(word2[i])
                i += 1

            while i < len1:
                result.append(word1[i])
                i += 1

        else:
            i = 0
            while i < len1:
                result.append(word1[i])
                result.append(word2[i])
                i += 1
            
            while i < len2:
                result.append(word2[i])
                i += 1

        return "".join(result)