
import pygame

SCREEN = pygame.display.set_mode((800, 600))

class VersusScreen:
    def __init__(self):
        self.load_bg_graphics()
        self.sparks_position = [-2327, -503]
        self.sparks_move_speed = 6

    def load_bg_graphics(self):
        self.bg = pygame.image.load("graphics/versus_screen/vsScreen_blackBg.png").convert_alpha()
        self.sparks = pygame.image.load("graphics/versus_screen/vsScreen_sparks.png").convert_alpha()

    def move_sparks(self):
        if self.sparks_position[0] >= 193 or self.sparks_position[1] <= -3023:
            self.sparks_position[0] = -3161
            self.sparks_position[1] = 327
        else:
            self.sparks_position[0] += self.sparks_move_speed
            self.sparks_position[1] -= self.sparks_move_speed

    def draw_bg(self):
        SCREEN.blit(self.bg, (0, 0))
        self.move_sparks()
        SCREEN.blit(self.sparks, self.sparks_position)