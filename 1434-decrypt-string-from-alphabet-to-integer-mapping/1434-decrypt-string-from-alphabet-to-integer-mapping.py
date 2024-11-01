class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = dict()
        result = []

        for i in range(97, 106):
            mapping[str(i - 96)] = chr(i)

        for i in range(106, 123):
            mapping[str(i-96) + chr(35)] = chr(i)

        n = len(s)
        j = 0
        while j < n-2:
            if s[j+2] == "#":
                result.append(mapping[s[j:j+3]])
                j += 3
            else:
                result.append(mapping[s[j]])
                j += 1

        while j < n:
            result.append(mapping[s[j]])
            j += 1

        return "".join(result)
