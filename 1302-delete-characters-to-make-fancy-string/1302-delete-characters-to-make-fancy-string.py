class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        if n < 3:
            return s

        stack = [s[0], s[1]]
        i = 2
        

        while i < n:
            if s[i] == s[i-1] and s[i] == s[i-2]:
                i += 1
                continue

            stack.append(s[i])
            i+=1

        return "".join(stack)
