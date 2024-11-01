class Solution:
    def getLucky(self, s: str, k: int) -> int:
        STR_TO_INT = {
            "a": "1", "b": "2", "c": "3", "d": "4", "e": "5", 
            "f": "6", "g": "7", "h": "8", "i": "9", "j": "10",
            "k": "11", "l": "12", "m": "13", "n": "14", "o": "15", 
            "p": "16", "q": "17", "r": "18", "s": "19", "t": "20",
            "u": "21", "v": "22", "w": "23", "x": "24", "y": "25", 
            "z": "26" 
        }

        result = ""

        for char in s:
            result += STR_TO_INT[char]

        for _ in range(k):
            previous_result = str(result)
            result = 0
            for num in previous_result:
                result += int(num)

        return result

