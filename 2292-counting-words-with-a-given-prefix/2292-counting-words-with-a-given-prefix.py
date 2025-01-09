class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        pref_length = len(pref)
        pref_count = 0

        for word in words:
            if len(word) < pref_length:
                continue

            if word[0:pref_length] == pref:
                pref_count += 1

        return pref_count