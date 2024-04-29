import pygame, sys
from pygame.locals import *
from piece import Piece

class Rook(Piece):
    def __init__(self, color, SIDE_L, num, board):
        w_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/WHITE_ROOK.png"
        b_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/BLACK_ROOK.png"
        x = 0 if num == 1 else 7
        y = 0 if color == "B" else 7
        Piece.__init__(self, color, w_img, b_img, SIDE_L, board, x, y, "Rook")


    def path(self, board, screen):
        self.PATH.clear()

        x = self.past_x
        y = self.past_y

        # RIGHT
        for i in range(7 - x):
            if self.check_path(board, screen, x + i + 1, y) == False:
                break
        # LEFT
        for i in range(x):
            if self.check_path(board, screen, x - i - 1, y) == False:
                break
        # UP
        for i in range(7 - y):
            if self.check_path(board, screen, x, y + i + 1) == False:
                break
        # DOWN
        for i in range(y):
            if self.check_path(board, screen, x, y - i - 1) == False:
                break
