class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []

        if n % 2 == 1:
            result = [i for i in range(-n//2+1, n//2 + 1)]

        else:
            for i in range(-n//2, 0):
                result.append(i)
                
            for i in range(1, n//2 + 1):
                result.append(i)

        return result


