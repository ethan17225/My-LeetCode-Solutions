class Solution:
    def compressedString(self, word: str) -> str:
        char = word[0]
        count = 1
        i = 1
        n = len(word)
        result = []

        while i < n:
            if char != word[i]:
                result.append(str(count) + char)
                char = word[i]
                count = 1
                i += 1
                continue

            if count < 9:
                count += 1
            else:
                result.append("9" + char)
                count = 1

            i += 1

        result.append(str(count) + char)

        return "".join(result)
