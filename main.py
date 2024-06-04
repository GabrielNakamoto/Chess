import pygame, sys, math
from pygame.locals import *
from player import Player
from pawn import Pawn

# ***** TO DO *****
# -> Checkmate check:

# add player function and check every turn
# if the king can move anywhere thats not in enemy paths
# (iterate enemy paths)
# then check if any of players pieces paths intersect with the check

# check for check and mate for both players!!

# -> Stalemate check
# -> add sounds

# -> Make castling work flipped and not?
# -> promote sound
# -> check sound takes priority

# -> select and click to move

# -> timers

# -> for border add an offset

# -> highlight selected piece
# -> highlight enemy last move
# -> dots for possible moves
# -> Promotion popup?
# -> settings menu?
# -> en passent
# -> numbers around edge + border?
# -> moves appear on side
# -> replay (hard)
# -> timer system
# *****************

CANVAS_L = 750
#WIDTH = CANVAS_L * 4/3
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
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 45)
screen = pygame.display.set_mode((CANVAS_L, CANVAS_L))

P1 = Player("W", SIDE_L, BOARD, 5)
P2 = Player("B", SIDE_L, BOARD, 5)

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
  '''
  if turn == "White" and pygame.time.get_ticks() - P1.past_time >= 1000:
    P1.tick()
    P1.past_time = pygame.time.get_ticks()
  elif turn == "Black" and pygame.time.get_ticks() - P2.past_time >= 1000:
    P2.tick()
    P2.past_time = pygame.time.get_ticks()
  '''
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



  #pygame.draw.rect(screen, (85,85,85), (CANVAS_L, 0, CANVAS_L * 1/3, CANVAS_L))
  # clocks
  '''
  pygame.draw.rect(screen, WHITE, (CANVAS_L, 0, CANVAS_L * 1/6, CANVAS_L * 1/12))
  text_surface = my_font.render(P1.get_time(), False, BLACK)
  screen.blit(text_surface, (CANVAS_L + 15, 0))
  pygame.draw.rect(screen, BLACK, (CANVAS_L * 7/6, 0, CANVAS_L * 1/6, CANVAS_L * 1/12))
  text_surface = my_font.render(P2.get_time(), False, WHITE)
  screen.blit(text_surface, (CANVAS_L * 7/6 + 15, 0))
  '''
  if select != False:
    select.draw(screen)


  pygame.display.update()

