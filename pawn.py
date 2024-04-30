import pygame, sys
from pygame.locals import *
from piece import Piece

class Pawn(Piece):
    def __init__(self, color, SIDE_L, num, board):
        w_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/WHITE_PAWN.png"
        b_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/BLACK_PAWN.png"
        x = num
        y = 1 if color == "B" else 6
        Piece.__init__(self, color, w_img, b_img, SIDE_L, board, x, y, "Pawn")

    def path(self, board, screen):

        self.PATH.clear()

        x = self.past_x
        y = self.past_y

        dy = 1 if self.color == "B" else -1

        if self.color == "B" and y == 1 or self.color == "W" and y == 6:
           cur = board[y + (dy * 2)][x]
           if cur == "X":
             self.PATH.append([x, y + (dy * 2)])

        if self.color == "W" and y > 0 or self.color == "B" and y < 7:
            cur = board[y + dy][x]
            if cur == "X":
                self.PATH.append([x, y + dy])

        if x > 0:
            if board[y + dy][ x - 1] != "X" and board[y + dy][ x - 1] != self.color and x > 0:
                self.PATH.append([x - 1, y + dy])

        if x < 7:
            if board[y + dy][ x + 1] != "X" and board[y + dy][ x + 1] != self.color:
                self.PATH.append([x + 1, y + dy])
