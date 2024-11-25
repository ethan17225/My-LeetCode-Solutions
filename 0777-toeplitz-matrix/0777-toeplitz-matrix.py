class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        i = 0
        n = len(matrix)
        m = len(matrix[0])

        while i < n - 1:
            if matrix[i][:m-1] != matrix[i+1][1:]:
                return False

            i += 1

        return True
