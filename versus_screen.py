
import pygame
from fonts import FONT_MASHEEN_30, FONT_MASHEEN_BOLD_40
from fonts import render

SCREEN = pygame.display.set_mode((800, 600))


class VersusScreen:
    def __init__(self, players: list):
        self.load_bg_graphic()
        self.align_sparks()
        self.players = players
        self.load_player_graphics()
        self.sparks_position = [-2327, -503]
        self.sparks_move_speed = 6

    def load_bg_graphic(self):
        self.bg = pygame.image.load("graphics/versus_screen/vsScreen_blackBg.png").convert_alpha()

    def load_player_graphics(self):
        self.player_graphics = []
        for player in self.players:
            self.player_graphics.append(pygame.image.load(f"graphics/player/{player}/vs_screen/{player}_vs_screen.png"))

    def align_sparks(self):
        self.aligned_sparks = []
        for spark_row in range(10):
            for i in range(7):
                self.aligned_sparks.append(Spark(i, "top-left", spark_row))
            for j in range(7):
                self.aligned_sparks.append(Spark(j, "bottom-right", spark_row))

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

        if len(self.aligned_sparks) <= 0:
            self.align_sparks()
        for spark in self.aligned_sparks:
            if spark.pos[0] > 670 and spark.pos[1] < -100:
                self.aligned_sparks.remove(spark)
            else: spark.draw()

        # player graphics
        for i in range(4):
            if i == 0:
                if self.players[i] == "yos":
                    x = 0
                else:
                    x = -40
            elif i == 1:
                if self.players[i] == "yos":
                    x = 200
                else:
                    x = 160
            elif i == 2:
                if self.players[i] == "yos":
                    x = 400
                else:
                    x = 360
            elif i == 3:
                if self.players[i] == "yos":
                    x = 600
                else:
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
            player_text_surface = render(player, FONT_MASHEEN_30, (240, 240, 240), (48, 48, 48), 2)
            player_text_surface_rect = player_text_surface.get_rect(center=(x_player_name[x_counter], Y))
            x_counter += 1
            SCREEN.blit(player_text_surface, player_text_surface_rect)

        # vs text
        vs_text_surface = render("VS", FONT_MASHEEN_BOLD_40, (223, 0, 0), (48, 48, 48), 2)
        x_vs_text = [210, 410, 610]
        for x in x_vs_text:
            vs_text_surface_rect = vs_text_surface.get_rect(center=(x, Y))
            SCREEN.blit(vs_text_surface, vs_text_surface_rect)

class Spark(pygame.sprite.Sprite):
    def __init__(self, no_in_row, direct, row_no):
        super().__init__()
        self.no_in_row = no_in_row
        self.direct = direct
        self.row_no = row_no
        self.DISTANCE = 60 # distance in px between the single sparks of a spark-row
        self.move_speed = 8
        self.find_pos()
        self.load_graphic()

    def find_pos(self):
        self.x = ((0 if self.row_no% 2 == 0 else -30) - (self.row_no * 95))
        self.y = ((600 if self.row_no % 2 == 0 else 570) + (self.row_no * 95))

        if self.direct == "top-left":
            self.pos = [(self.x - (self.no_in_row * self.DISTANCE)), (self.y - (self.no_in_row * self.DISTANCE))]
        else:
            self.pos = [(self.x + (self.no_in_row * self.DISTANCE)), (self.y + (self.no_in_row * self.DISTANCE))]

    def load_graphic(self):
        self.spark = pygame.image.load("graphics/versus_screen/vsScreen_spark.png").convert_alpha()

    def move(self):
        self.pos[0] += self.move_speed
        self.pos[1] -= self.move_speed

    def draw(self):
        SCREEN.blit(self.spark, self.pos)
        self.move()