class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        i = dia_sum = 0 

        if n == 1:
            return mat[0][0]

        if n % 2 == 1:
            middle = n // 2

            while i < middle:
                j = -i - 1

                dia_sum += sum_all(mat, i, j)

                i += 1

            dia_sum += mat[middle][middle]

        else:
            middle = n // 2 - 1

            while i <= middle:
                j = -i - 1

                dia_sum += sum_all(mat, i, j)

                i += 1

        return dia_sum


def sum_all(mat, i, j):
    return mat[i][i] + mat[i][j] + mat[j][i] + mat[j][j]
