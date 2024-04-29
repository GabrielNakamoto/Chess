import pygame, sys
from pygame.locals import *
from piece import Piece

class Queen(Piece):
    def __init__(self, color, SIDE_L, board):
        w_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/WHITE_QUEEN.png"
        b_img = "/Users/gabrielnakamoto/Desktop/projects/ChessPy/images/BLACK_QUEEN.png"
        x = 3
        y = 0 if color == "B" else 7
        Piece.__init__(self, color, w_img, b_img, SIDE_L, board, x, y, "Queen")

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
