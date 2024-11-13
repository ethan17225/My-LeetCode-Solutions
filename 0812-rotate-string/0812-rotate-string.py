class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        i = 0

        while i < n:
            if s[i] != goal[0]:
                i += 1
                continue

            if s[i:] + s[0:i] == goal:
                return True

            i += 1

        return False