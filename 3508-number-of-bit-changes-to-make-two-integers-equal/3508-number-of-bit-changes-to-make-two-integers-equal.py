class Solution:
    def minChanges(self, n: int, k: int) -> int:
        n_bins = [num for num in bin(n)[2:]]
        k_bins = [num for num in bin(k)[2:]]

        while len(n_bins) < len(k_bins):
            n_bins.insert(0, "0")

        while len(k_bins) < len(n_bins):
            k_bins.insert(0, "0")
        

        count = 0
        for b1, b2 in zip(n_bins, k_bins):
            if b1 == b2:
                continue

            if b1 == "0" and b2 == "1":
                return - 1

            count += 1

        return count