class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        track_dict = dict()

        nums_list = [set(nums1), set(nums2), set(nums3)]

        for nums in nums_list:
            for num in nums:
                track_dict[num] = track_dict.get(num, 0) + 1


        result = []
        for num, count in track_dict.items():
            if count >= 2:
                result.append(num)

        return result