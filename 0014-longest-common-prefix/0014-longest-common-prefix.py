class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs_len = len(strs)
        if strs_len == 0:
            return ""

        if strs_len == 1:
            return strs[0]

        prefix = ""
        s0_len = len(strs[0])
        s1_len = len(strs[1])
        i = 0

        while i < s1_len and i < s0_len:
            if strs[0][i] == strs[1][i] and i < s1_len:
                prefix += strs[0][i]
                i+=1
            
            else:
                if prefix == "":
                    return ""
                
                break

        for i in range(2, len(strs)):
            si_len = len(strs[i])
            if si_len == 0:
                return ""

            if si_len >= len(prefix): 
                for k in range(len(prefix)):
                    if prefix[k] != strs[i][k]:
                        if k == 0:
                            return ""

                        prefix = prefix[:k]
                        break

            else:
                for k in range(len(strs[i])):
                    if si_len == 1:
                        if prefix[k] != strs[i][k]:
                            return ""

                        else:
                            prefix = strs[i][k]
                            break


                    if prefix[k] != strs[i][k]:
                        if k == 0:
                            return ""

                        prefix = prefix[:k]
                        break

        return prefix

        

         





        