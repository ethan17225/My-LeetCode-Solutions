class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]

            return

        nums1[m:] = nums2

        nums1.sort()