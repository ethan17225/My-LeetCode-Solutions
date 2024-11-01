class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        matrix = []
        for c in range(n):
            matrix.append([])

        for i in range(len(matrix)):
            for j in range(n):
                matrix[i].append((i*n) + j)
                    
        current = [0,0]
        for command in commands:
            match command:
                case "UP":
                    current[0] -= 1

                case "DOWN":
                    current[0] += 1

                case "LEFT":
                    current[1] -= 1
                        
                case "RIGHT":
                    current[1] +=1

        return matrix[current[0]][current[1]]
    