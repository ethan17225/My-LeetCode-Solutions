class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        char_map = dict()

        k = 97

        for char in key:
            if char == " " or char in char_map:
                continue

            char_map[char] = chr(k)
            k += 1
        
        encode_mess = []
        for char in message:
            if char == " ":
                encode_mess.append(char)
                continue

            encode_mess.append(char_map[char])

        return "".join(encode_mess)

            