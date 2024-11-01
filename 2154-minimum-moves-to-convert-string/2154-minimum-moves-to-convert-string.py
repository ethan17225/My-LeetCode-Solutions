class Solution:
    def minimumMoves(self, s: str) -> int:
        steps = 0
        chars = [c for c in s]
        length = len(s)
        
        if "X" not in s:
            return 0

        i = 0
        while i + 2 < length:
            if "X" in chars[i:i+3]:
                while chars[i] == "O" and i + 2 < length:
                    i+=1
                steps += 1
                chars[i:i+3] = ["O"] * 3
                i += 1
            else:
                i += 1

            

        return steps
