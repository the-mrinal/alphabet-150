class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix = [["" for _ in range(3)] for _ in range(3)]
        
        def checkMatrix(x,y):
            if x == y:
                if matrix[0][0] == matrix[1][1]:
                    if matrix[1][1] == matrix[2][2]:
                        return True
            if ((x == 0 and y == 2) or (x == 2 and y == 0)) or (x == 1 and y == 1):
                if matrix[0][2] == matrix[1][1]:
                    if matrix[1][1] == matrix[2][0]:
                        return True
            if matrix[0][y] == matrix[1][y]:
                if matrix[1][y] == matrix[2][y]:
                    return True
            if matrix[x][0] == matrix[x][1]:
                if matrix[x][1] == matrix[x][2]:
                    return True
            return False
        
        for index,(x,y) in enumerate(moves):
            matrix[x][y] = 'O' if index % 2 != 0 else 'X'
            if checkMatrix(x,y):
                return 'B' if index % 2 != 0 else 'A'
        
        return 'Draw' if len(moves) == 9 else 'Pending'