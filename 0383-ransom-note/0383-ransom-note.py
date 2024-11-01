from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)

        for key in counter1.keys():
            if key not in counter2:
                return False

            if counter1[key] > counter2[key]:
                return False

        return True

        
