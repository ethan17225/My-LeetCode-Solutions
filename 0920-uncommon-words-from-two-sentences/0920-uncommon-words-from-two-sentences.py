class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()
        result = []

        freq = dict()

        for w1 in words1:
            freq[w1] = freq.get(w1, 0) + 1

        for w2 in words2:
            freq[w2] = freq.get(w2, 0) + 1

        for word, count in freq.items():
            if count == 1:
                result.append(word)

        return result
        