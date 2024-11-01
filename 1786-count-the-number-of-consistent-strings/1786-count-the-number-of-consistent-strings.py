class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed_chars = set(allowed)

        for word in words:
            if all(char in allowed_chars for char in word):
                count += 1

        return count