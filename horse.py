import pygame, sys
from pygame.locals import *
from piece import Piece

class Horse(Piece):
    def __init__(self, color, SIDE_L, num, board):
        w_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/WHITE_HORSE.png"
        b_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/BLACK_HORSE.png"
        x = 1 if num == 1 else 6
        y = 0 if color == "B" else 7
        Piece.__init__(self, color, w_img, b_img, SIDE_L, board, x, y, "Horse")

    def path(self, board, screen):

        self.PATH.clear()

        x = self.past_x
        y = self.past_y
        if y - 2 >= 0 and x - 1 >= 0:
            self.check_path(board, screen, x - 1, y - 2)
        if y - 2 >= 0 and x + 1 <= 7:
            self.check_path(board, screen, x + 1, y - 2)
        if y + 2 <= 7 and x - 1 >= 0:
            self.check_path(board, screen, x - 1, y + 2)
        if y + 2 <= 7 and x + 1 <= 7:
            self.check_path(board, screen, x + 1, y + 2)
        if x - 2 >= 0 and y - 1 >= 0:
            self.check_path(board, screen, x - 2, y - 1)
        if x - 2 >= 0 and y + 1 <= 7:
            self.check_path(board, screen, x - 2, y + 1)
        if x + 2 <= 7 and y - 1 >= 0:
            self.check_path(board, screen, x + 2, y - 1)
        if x + 2 <= 7 and y + 1 <= 7:
            self.check_path(board, screen, x + 2, y + 1)
