import pygame, sys
from pygame.locals import *
from player import Player
from pawn import Pawn

# ***** TO DO *****
# -> Checkmate check:

# add player function and check every turn
# if the king can move anywhere thats not in enemy paths
# (iterate enemy paths)
# then check if any of players pieces paths intersect with the check

# -> Promotion choice (make a popup?)
# -> castling (boolean in king that is true before first move)
# -> en passent
# -> numbers around edge + border?
# -> moves appear on side
# -> replay (hard)
# -> timer system
# *****************

CANVAS_L = 750
SIDE_L = CANVAS_L / 8

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DARK = (118,150,86)
LIGHT = (238,238,210)

GRID = []
BOARD = []

for row in range(8):
    ROW = []
    BOARD_ROW = []
    for col in range(8):
        ROW.append(pygame.Rect(col * SIDE_L, row * SIDE_L, SIDE_L, SIDE_L))
        BOARD_ROW.append("X")
    GRID.append(ROW)
    BOARD.append(BOARD_ROW)

pygame.init()
screen = pygame.display.set_mode((CANVAS_L, CANVAS_L))

P1 = Player("W", SIDE_L, BOARD)
P2 = Player("B", SIDE_L, BOARD)

select = False

turn = "White"

clock = pygame.time.Clock()
pygame.display.set_caption('Chess')
while True:
  clock.tick(60)
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == MOUSEBUTTONDOWN:
      select = P1.select_piece(BOARD) if turn == "White" else P2.select_piece(BOARD)
    if event.type == MOUSEBUTTONUP and select != False:
      if turn == "White" and select.snap(BOARD, P2, P1, screen):
          turn = "Black"
      elif select.snap(BOARD, P1, P2, screen):
          turn = "White"
      select = False

  screen.fill(LIGHT)

  for row in range(8):
    color = LIGHT if row % 2 == 0 else DARK
    for col in range(8):
        rect = GRID[row][col]
        pygame.draw.rect(screen, color, rect)
        color = LIGHT if color == DARK else DARK

  if select != False:
    select.drag(BOARD, screen)

  P1.draw(screen)
  P2.draw(screen)

  if select != False:
    select.draw(screen)


  pygame.display.update()
