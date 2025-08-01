class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(1, numRows):
            temp = [1]
            previous_arr = result[i-1]
            n = len(previous_arr)
            j = 0

            while j < n - 1:
                temp.append(previous_arr[j] + previous_arr[j+1])
                j += 1

            temp.append(1)
            result.append(temp)

        return result



