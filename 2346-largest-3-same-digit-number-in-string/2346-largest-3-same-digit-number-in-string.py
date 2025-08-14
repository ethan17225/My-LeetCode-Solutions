class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        max_num = -1
        max_string = ""

        if n < 3:
            return ""

        i = 0
        while i + 2 < n:
            if num[i] == num[i+1] and num[i] == num[i+2]:
                temp = int(num[i:i+3])
                if max_num < temp:
                    max_num = temp
                    max_string = num[i:i+3]
                i += 2
            i += 1

        return max_string
