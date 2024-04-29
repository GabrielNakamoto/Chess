import pygame, sys
from pygame.locals import *
from rook import Rook
from horse import Horse
from bishop import Bishop
from pawn import Pawn
from king import King
from queen import Queen

class Player:
    def __init__(self, color, SIDE_L, board):
        self.color = color
        self.pieces = []
        self.r1 = Rook(color, SIDE_L, 1, board)
        self.r2 = Rook(color, SIDE_L, 2, board)
        self.b1 = Bishop(color, SIDE_L, 1, board)
        self.b2 = Bishop(color, SIDE_L, 2, board)
        self.h1 = Horse(color, SIDE_L, 1, board)
        self.h2 = Horse(color, SIDE_L, 2, board)
        self.k = King(color, SIDE_L, board)
        self.q = Queen(color, SIDE_L, board)
        self.pawns = []
        for i in range(8):
            self.pawns.append(Pawn(color, SIDE_L, i, board))
            self.pieces.append(Pawn(color, SIDE_L, i, board))
        self.pieces.extend([self.r1, self.r2, self.h1, self.h2, self.b1, self.b2, self.k, self.q])

    def draw(self, screen):
        for piece in self.pieces:
            piece.draw(screen)

    def select_piece(self, board):
        for piece in self.pieces:
            if piece.rect.collidepoint(pygame.mouse.get_pos()):
                board[piece.y][piece.x] = "X"
                piece.past_x = piece.x
                piece.past_y = piece.y
                return piece
        return False

    def promote(self, pawn, board, type):
        # add promotion type paramater and filled bool
        self.pieces.remove(pawn)
        filled = False
        if board[7][3] == self.color:
            filled = True
        if type == "Queen":
            new_piece = Queen(self.color, pawn.SIDE_L, board)
        elif type == "Rook":
            new_piece = Rook(self.color, pawn.SIDE_L, 1, board)
        elif type == "Bishop":
            new_piece = Bishop(self.color, pawn.SIDE_L, 1, board)
        elif type == "Horse":
            new_piece = Horse(self.color, pawn.SIDE_L, 1, board)
        self.pieces.append(new_piece)
        new_piece = self.pieces[-1]
        if not filled:
            board[new_piece.y][new_piece.x] = "X"
        new_piece.x = pawn.x
        new_piece.y = pawn.y
        new_piece.past_x = pawn.x
        new_piece.past_y = pawn.y
        new_piece.rect = pygame.Rect(new_piece.x * new_piece.SIDE_L, new_piece.y * new_piece.SIDE_L, new_piece.SIDE_L, new_piece.SIDE_L)


