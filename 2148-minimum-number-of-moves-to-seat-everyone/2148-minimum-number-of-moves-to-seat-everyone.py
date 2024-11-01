class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)

        total_moves = 0
        for seat, student in zip(sorted_seats, sorted_students):
            total_moves += abs(seat - student)

        return total_moves