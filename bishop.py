import pygame, sys
from pygame.locals import *
from piece import Piece

class Bishop(Piece):
    def __init__(self, color, SIDE_L, num, board):
        w_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/WHITE_BISHOP.png"
        b_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/BLACK_BISHOP.png"
        x = 2 if num == 1 else 5
        y = 0 if color == "B" else 7
        Piece.__init__(self, color, w_img, b_img, SIDE_L, board, x, y, "Bishop")

    def path(self, board, screen):

        self.PATH.clear()

        x = self.past_x
        y = self.past_y

        # DOUBLE POINTER?

        for i in range(x):
            if y - i - 1 < 0:
              break
            if self.check_path(board, screen, x - i - 1, y - i - 1) == False:
              break

        for i in range(x):
          if y + i + 1 > 7:
            break
          if self.check_path(board, screen, x - i - 1, y + i + 1) == False:
              break

        for i in range(7 - x):
          if y + i + 1 > 7:
            break
          if self.check_path(board, screen, x + i + 1, y + i + 1) == False:
            break

        for i in range(7 - x):
          if y - i - 1 > 7:
            break
          if self.check_path(board, screen, x + i + 1, y - i - 1) == False:
            break
