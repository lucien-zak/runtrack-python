import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)


class TicTacToe:
    def __init__(self):
        self.board: list[list] = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.player: int = 1
        self.winner: int = 0
        self.turn: int = 0
        self.canPlay: bool = True
        self.endGame: bool = False

    def print(self) -> None:
        for row in self.board:
            print(row)

    def playFromMouse(self, x, y):
        if x < 200 and y < 200:
            self.play(0, 0)
        elif x < 400 and y < 200:
            self.play(0, 1)
        elif x < 600 and y < 200:
            self.play(0, 2)
        elif x < 200 and y < 400:
            self.play(1, 0)
        elif x < 400 and y < 400:
            self.play(1, 1)
        elif x < 600 and y < 400:
            self.play(1, 2)
        elif x < 200 and y < 600:
            self.play(2, 0)
        elif x < 400 and y < 600:
            self.play(2, 1)
        elif x < 600 and y < 600:
            self.play(2, 2)
        self.print()

    def play(self, x, y):
        print('Joueur', self.player, 'joue en', x, y)
        if self.board[x][y] == 0 and self.canPlay:
            self.canPlay = True
            self.board[x][y] = self.player
            self.player = 2 if self.player == 1 else 1
            self.turn += 1
            self.check()
        else:
            self.canPlay = False
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
            self.canPlay = False
            self.endGame = True
        elif self.turn == 9:
            self.endGame = True
            print('Match nul')
        
    def returnPlayer(self):
        if self.winner == 1 or self.player == 2:
            return "O"
        elif (self.winner == 2 or self.player == 1):
            return "X"


pygame.init()
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((HEIGHT, WIDTH))
window.fill(GREY)
pygame.draw.line(window, WHITE, (200, 0), (200, 600), 5)
pygame.draw.line(window, WHITE, (400, 0), (400, 600), 5)
pygame.draw.line(window, WHITE, (0, 200), (600, 200), 5)
pygame.draw.line(window, WHITE, (0, 400), (600, 400), 5)
pygame.display.set_caption("Jeu du morpion")
start = 1
game = TicTacToe()
font = pygame.font.Font(None, 52)
second = 5000
while start:
    for event in pygame.event.get():
        if event.type == QUIT:
            start = 0
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                start = 0
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] < 200:
                    x = 0
                elif event.pos[0] < 400:
                    x = 200
                else:
                    x = 400
                if event.pos[1] < 200:
                    y = 0
                elif event.pos[1] < 400:
                    y = 200
                else:
                    y = 400
                game.playFromMouse(event.pos[0], event.pos[1])
                if game.canPlay:
                    rect = pygame.Rect(x, y, 200, 200)
                    text = font.render(game.returnPlayer(),1,(0,0,255))
                    window.blit(text, (x + 100, y + 100))
                if game.winner != 0 and game.endGame == True:
                    if game.turn == 9:
                        text = font.render("Match nul",1,(255,255,255))
                    else:
                        text = font.render(f"Le joueur {game.returnPlayer()} a gagné, il reste {second} secondes",1,(255,255,255))
                        second -= 1
                    window.blit(text, (WIDTH / 2 - (text.get_width() / 2), HEIGHT / 2))
                    if game.player == 1:
                        text = font.render("X",1,(255,0,0))
                        window.blit(text, (x + 100, y + 100))
                    else:
                        text = font.render("O",1,(0,0,255))
                        window.blit(text, (x + 100, y + 100))
                    # restart the game with a button
                    button = pygame.Rect(0, 0, 200, 50)
                    pygame.draw.rect(window, (255, 0, 0), button)
                    text = font.render("Restart",1,(255,255,255))
                    window.blit(text, (100 - (text.get_width() / 2), 25 - (text.get_height() / 2)))
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if event.pos[0] < 200 and event.pos[1] < 50:
                                game = TicTacToe()
                                window.fill(GREY)
                                pygame.draw.line(window, WHITE, (200, 0), (200, 600), 5)
                                pygame.draw.line(window, WHITE, (400, 0), (400, 600), 5)
                                pygame.draw.line(window, WHITE, (0, 200), (600, 200), 5)
                                pygame.draw.line(window, WHITE, (0, 400), (600, 400), 5)
                                pygame.display.update()
    pygame.display.flip()
pygame.quit()




