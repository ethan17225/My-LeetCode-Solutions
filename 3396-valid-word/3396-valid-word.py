class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        counter = {
            "vowel": 0,
            "consonant": 0,
        }

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    counter["vowel"] += 1

                else:
                    counter["consonant"] += 1

            elif not c.isdigit():
                return False

        return True if counter["vowel"] > 0 and counter["consonant"] > 0 else False
