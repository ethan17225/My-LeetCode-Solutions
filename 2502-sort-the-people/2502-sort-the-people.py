class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        user_heights = []
        for i in range(len(names)):
            user_heights.append((names[i], heights[i]))

        sorted_user_heights = sorted(user_heights, key = lambda item: item[1], reverse=True)

        i = 0
        for user, height in sorted_user_heights:
            names[i] = user
            i += 1

        return names
