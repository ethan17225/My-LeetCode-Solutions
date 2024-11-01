class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_num = len(matrix)

        for i in range(row_num):
            min_num = min(matrix[i])
            j = matrix[i].index(min_num)
            
            col = [matrix[k][j] for k in range(row_num)]
            max_num = max(col)

            if min_num == max_num:
                return [min_num]
            


            
        