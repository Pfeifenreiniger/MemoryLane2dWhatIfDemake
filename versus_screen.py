
import pygame

SCREEN = pygame.display.set_mode((800, 600))

class VersusScreen:
    def __init__(self, players: list):
        self.load_bg_graphics()
        self.load_player_graphics(players)
        self.sparks_position = [-2327, -503]
        self.sparks_move_speed = 6

    def load_bg_graphics(self):
        self.bg = pygame.image.load("graphics/versus_screen/vsScreen_blackBg.png").convert_alpha()
        self.sparks = pygame.image.load("graphics/versus_screen/vsScreen_sparks.png").convert_alpha()


    def load_player_graphics(self, players):
        self.player_graphics = []
        for player in players:
            self.player_graphics.append(pygame.image.load(f"graphics/player/{player}/vs_screen/{player}_vs_screen.png"))

    def move_sparks(self):
        if self.sparks_position[0] >= 193 or self.sparks_position[1] <= -3023:
            self.sparks_position[0] = -3161
            self.sparks_position[1] = 327
        else:
            self.sparks_position[0] += self.sparks_move_speed
            self.sparks_position[1] -= self.sparks_move_speed

    def draw(self):
        # animated bg
        SCREEN.blit(self.bg, (0, 0))
        self.move_sparks()
        SCREEN.blit(self.sparks, self.sparks_position)

        # player graphics
        for i in range(4):
            if i == 0:
                x = -40
            elif i == 1:
                x = 160
            elif i == 2:
                x = 360
            elif i == 3:
                x = 560
            SCREEN.blit(self.player_graphics[i], (x, 0))