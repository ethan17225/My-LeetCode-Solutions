class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        sums = dict()

        if n < 4:
            return 0

        for i in range(n):
            for j in range(i+1,n):
                t = nums[i]*nums[j]
                sums[t] = sums.get(t,0) + 1

        k = 0
        for v in sums.values():
            if v == 2:
                k += 1
                continue

            if v > 2:
                k += sum(i for i in range(1,v))

        return k * 8

        
 
        