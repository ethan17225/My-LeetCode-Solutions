class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)

        if n == 1:
            w = words[0]
            return w[0] == w[len(w) - 1]

        i = 0
        while i < n-1:
            w1 = words[i]
            w2 = words[i+1]

            if w1[len(w1) - 1] != w2[0]:
                return False

            i += 1

        w_first = words[0]
        w_last = words[n-1]

        return True if w_last[len(w_last) - 1] == w_first[0] else False