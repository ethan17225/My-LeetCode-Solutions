class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        list_2d = []
        length = len(original)

        if m*n != length:
            return []

        for row in range(m):
            list_2d.append([original[col] for col in range(row*n, (row+1)*n)])
    
        return list_2d

