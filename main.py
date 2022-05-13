'''
2D pixelart what-if demake of the Mario Party 6 minigame Memory Lane (https://mario.fandom.com/wiki/Memory_Lane).

Imagine Nintendo's Super Mario IP would have been heavily influenced by the 1993 theatrical movie Super Mario Bros.
(https://en.wikipedia.org/wiki/Super_Mario_Bros._(film)) and the Mario Party games would more be like a kind of
violent battle royal as seen in the 1987 movie The Running Man with Arnold Schwarzenegger (https://en.wikipedia.org/wiki/The_Running_Man_(1987_film)).

Code and graphics by Kevin Spathmann (Pfeifenreiniger on GitHub: https://github.com/Pfeifenreiniger)
Fonts used: ?????
Musics, SFX, and voices used ????
Original Game (included in Mario Party 6) by Hudson Soft™ and Nintendo™
'''

import pygame, sys
from versus_screen import VersusScreen

pygame.init()

##----------------------------DISPLAY SCREEN----------------------------##

SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Memory Lane 2D What-If-Demake")
#TODO: Create an icon
# ICON = pygame.image.load("graphics/game_icon.png").convert_alpha()
# pygame.display.set_icon(ICON)
clock = pygame.time.Clock()
FPS = 30

##----------------------------VS SCREEN----------------------------##
vs_screen = VersusScreen()

##----------------------------GAMELOOP----------------------------##
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    vs_screen.draw_bg()



    pygame.display.set_caption("Memory Lane 2D What-If-Demake | " + str(round(clock.get_fps())) + " FPS")
    pygame.display.update()
    clock.tick(FPS)