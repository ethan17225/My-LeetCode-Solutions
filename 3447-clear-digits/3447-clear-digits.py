class Solution:
    def clearDigits(self, s: str) -> str:
        clear_strings = []
        chars = [char for char in s]

        i = 0

        while i < len(chars):
            if chars[i].isdigit():
                digit_count = 1
                while i < len(chars) - digit_count and chars[i+digit_count].isdigit():
                    digit_count += 1

                if i - digit_count <= 0:
                    chars = chars[i+digit_count:]
                    i = 0
                    continue
                elif i - digit_count == 1:
                    chars = [chars[0]] + chars[i+digit_count:]
                    i = 1
                    continue
                else:
                    chars = chars[0:i-digit_count] + chars[i+digit_count:]
                    i = i-digit_count

            i+=1

        return "".join(chars)