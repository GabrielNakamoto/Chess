import pygame, sys
from pygame.locals import *
from piece import Piece

class King(Piece):
    def __init__(self, color, SIDE_L, board):
        w_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/WHITE_KING.png"
        b_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/BLACK_KING.png"
        x = 4
        y = 0 if color == "B" else 7
        Piece.__init__(self, color, w_img, b_img, SIDE_L, board, x, y, "King")

    def path(self, board, screen):

        self.PATH.clear()

        x = self.past_x
        y = self.past_y

        if y > 0:
            self.check_path(board, screen, x, y - 1)
            if x > 0:
                self.check_path(board, screen, x - 1, y - 1)
            if x < 7:
                self.check_path(board, screen, x + 1, y - 1)
        if y < 7:
            self.check_path(board, screen, x, y + 1)
            if x > 0:
                self.check_path(board, screen, x - 1, y + 1)
            if x < 7:
                self.check_path(board, screen, x + 1, y + 1)
        if x > 0:
            self.check_path(board, screen, x - 1, y)

        if x < 7:
            self.check_path(board, screen, x + 1, y)
