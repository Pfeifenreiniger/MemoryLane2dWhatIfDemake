
import pygame
from fonts import FONT_MASHEEN_30, FONT_MASHEEN_BOLD_40

SCREEN = pygame.display.set_mode((800, 600))

class VersusScreen:
    def __init__(self, players: list):
        self.load_bg_graphics()
        self.players = players
        self.load_player_graphics()
        self.sparks_position = [-2327, -503]
        self.sparks_move_speed = 6

    def load_bg_graphics(self):
        self.bg = pygame.image.load("graphics/versus_screen/vsScreen_blackBg.png").convert_alpha()
        self.sparks = pygame.image.load("graphics/versus_screen/vsScreen_sparks.png").convert_alpha()


    def load_player_graphics(self):
        self.player_graphics = []
        for player in self.players:
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

        # player text
        Y = 450
        x_player_name = [110, 310, 510, 710]
        x_counter = 0
        for player in self.players:
            if player == "mar":
                player = "Mario"
            elif player == "lui":
                player = "Luigi"
            elif player == "pea":
                player = "Peach"
            elif player == "yos":
                player = "Yoshi"
            player_text_surface = FONT_MASHEEN_30.render(player, False, (240, 240, 240))
            player_text_surface_rect = player_text_surface.get_rect(center=(x_player_name[x_counter], Y))
            x_counter += 1
            SCREEN.blit(player_text_surface, player_text_surface_rect)

        # vs text
        vs_text_surface = FONT_MASHEEN_BOLD_40.render("VS", False, (223, 0, 0))
        x_vs_text = [210, 410, 610]
        for x in x_vs_text:
            vs_text_surface_rect = vs_text_surface.get_rect(center=(x, Y))
            SCREEN.blit(vs_text_surface, vs_text_surface_rect)

