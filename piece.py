import pygame, sys
from pygame.locals import *

class Piece:
    def __init__(self, color, w_img, b_img, SIDE_L, board, x, y, type):
        self.type = type
        self.color = color
        self.SIDE_L = SIDE_L
        self.img_src = w_img if color == "W" else b_img
        self.img = pygame.image.load(self.img_src).convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.SIDE_L, self.SIDE_L))
        self.x = x
        self.y = y
        self.past_x = x
        self.past_y = y
        self.rect = pygame.Rect(x * self.SIDE_L, y * self.SIDE_L, SIDE_L, SIDE_L)
        board[self.y][self.x] = self.color
        self.PATH = []

    def draw(self, screen):
        screen.blit(self.img, (self.x * self.SIDE_L, self.y * self.SIDE_L))

    def drag(self, board, screen):
        self.x = (pygame.mouse.get_pos()[0] - self.SIDE_L / 2) / self.SIDE_L
        self.y = (pygame.mouse.get_pos()[1] - self.SIDE_L / 2) / self.SIDE_L
        self.rect = pygame.Rect(self.x * self.SIDE_L, self.y * self.SIDE_L, self.SIDE_L, self.SIDE_L)
        self.path(board, screen)

    def snap(self, board, opponent, player):
        self.x = round(self.x)
        self.y = round(self.y)
        output = True
        if not [self.x, self.y] in self.PATH or board[self.y][self.x] == self.color:
            self.x = self.past_x
            self.y = self.past_y
            output = False
        elif self.x == self.past_x and self.y == self.past_y:
            output = False
        elif board[self.y][self.x] != "X":
            for piece in opponent.pieces:
                if piece.rect.collidepoint(pygame.mouse.get_pos()):
                    opponent.pieces.remove(piece)
                    break
        if self.type == "Pawn":
            if self.color == "W" and self.y == 0 or self.color == "B" and self.y == 7:
                pygame.event.wait()
                keys = pygame.key.get_pressed()
                choice = " "
                while choice == " ":
                    pygame.event.wait()
                    keys = pygame.key.get_pressed()
                    if keys[K_q]:
                        choice = "Queen"
                    elif keys[K_h]:
                        choice = "Horse"
                    elif keys[K_r]:
                        choice = "Rook"
                    elif keys[K_b]:
                        choice = "Bishop"
                player.promote(self, board, choice)
        self.past_x = self.x
        self.past_y = self.y
        self.rect = pygame.Rect(self.x * self.SIDE_L, self.y * self.SIDE_L, self.SIDE_L, self.SIDE_L)
        board[self.y][self.x] = self.color
        return output

    def check_path(self, board, screen, x_target, y_target):
        cur = board[y_target][x_target]
        if cur == self.color:
            return False
        self.PATH.append([x_target, y_target])
        if cur != "X":
            return False