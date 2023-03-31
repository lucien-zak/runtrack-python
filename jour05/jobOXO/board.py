class TicTacToe:
    def __init__(self):
        self.board :list[list] = [[0, 0, 0], 
                      [0, 0, 0], 
                      [0, 0, 0]]
        self.player: int = 1
        self.winner: int = 0
        self.turn: int = 0
        self.running: bool = True

    def print(self) -> None:
        for row in self.board:
            print(row)
    
    def play(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] = self.player
            self.player = 2 if self.player == 1 else 1
            self.turn += 1
            self.check()
        else:
            print('Case déjà prise')
    
    def check(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != 0:
                self.winner = row[0]
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.winner = self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.winner = self.board[0][2]
        if self.winner != 0:
            print('Le joueur', self.winner, 'a gagné')
        elif self.turn == 9:
            print('Match nul')

test = TicTacToe()
test.play(0, 0)
test.play(0, 1)
test.play(1, 1)
test.play(0, 2)
test.play(2, 2)
test.print()

