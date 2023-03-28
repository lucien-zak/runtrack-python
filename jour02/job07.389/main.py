class Puissance4:

    def __init__(self, i, j):
            self.board = [['O' for column in range(j)] for line in range(i)]
            self.width = j
            self.height = i
    def print(self):
        for row in self.board[::-1]:
            print(row)

    def play(self, column: int, player: str):
        for row in self.board:
            if row[column] == "O":
                row[column] = player
                break
        print("Joueur " + player + " à joué dans la colonne " + str(column) + ".")
        if self.winCheck():
            print("Le joueur " + player + " a gagné !")
            exit()

    def winCheck(self):
        for row in self.board:
            for column in range(self.width - 3):
                if row[column] == row[column + 1] == row[column + 2] == row[column + 3] != "O":
                    return True
        for column in range(self.width):
            for row in range(self.height - 3):
                if self.board[row][column] == self.board[row + 1][column] == self.board[row + 2][column] == self.board[row + 3][column] != "O":
                    return True
        for row in range(self.height - 3):
            for column in range(self.width - 3):
                if self.board[row][column] == self.board[row + 1][column + 1] == self.board[row + 2][column + 2] == self.board[row + 3][column + 3] != "O":
                    return True
        for row in range(self.height - 3):
            for column in range(self.width - 3):
                if self.board[row][column + 3] == self.board[row + 1][column + 2] == self.board[row + 2][column + 1] == self.board[row + 3][column] != "O":
                    return True
        return False
    
class AI_One:
    def __init__(self, player):
        self.player = player
    
    def think(self, board: Puissance4):
        played :list = []
        for column in range(board.width):
            for row in range(board.height):
                if board.board[row][column] == self.player:
                    played.append([row, column])
        if played == [] and board.board[0][5] == "O":
            board.play(5, self.player)
        else:
            for row in range(board.height):
                for column in range(board.width):
                    if board.board[row][column] == "O":
                        board.play(column, self.player)
                        return
       
    
         


puissance4 = Puissance4(10, 10)
for i in range(100):
    AI_One("R").think(puissance4)
    AI_One("B").think(puissance4)
    puissance4.print()
