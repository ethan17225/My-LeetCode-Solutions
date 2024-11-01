class Solution:
    def makeFancyString(self, s: str) -> str:
        chars = []
        i = 0
        j = 1
        n = len(s)

        while j < n:
            if s[i] == s[j]:
                chars.append(s[i])
                chars.append(s[j])
                j += 1

                while j < n:
                    if s[i] == s[j]:
                        j += 1
                    else:
                        break

            else:
                chars.append(s[i])

            i = j
            j += 1

        if i < n:
            chars.append(s[i])

        

        

        return "".join(chars)