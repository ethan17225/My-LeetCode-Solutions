class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = consonant = 0

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    vowel += 1

                else:
                    consonant += 1

            elif not c.isdigit():
                return False

        return True if vowel > 0 and consonant > 0 else False
