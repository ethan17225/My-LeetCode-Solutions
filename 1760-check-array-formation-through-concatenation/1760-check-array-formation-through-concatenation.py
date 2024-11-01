class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arr_len = len(arr)

        for piece in pieces:
            if type(piece) == int:
                return True if piece in arr else False

            else:
                if piece[0] in arr:
                    i = arr.index(piece[0])

                else:
                    return False

                for num in piece[1:]:
                    i += 1
                    if i >= arr_len:
                        return False

                    if num != arr[i]:
                        return False

        return True
            