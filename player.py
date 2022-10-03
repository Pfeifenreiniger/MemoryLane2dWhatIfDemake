
from main import pygame, SCREEN, random
from stage import ShyGuy
from tiles_field_borders import borders


PLAYER_SPRITE_ORIG_SCALE = (68, 75)
SHADOW_SPRITE_ORIG_SCALE = (68, 25)

class Player(ShyGuy):
    def __init__(self, char:str, pnum:int, cpu:bool):
        self.sprites = self.load_sprites("graphics/player", char)
        self.pnum = pnum
        self.x = 365
        self.y = 520
        self.pos = (self.x, self.y)
        self.current_row = 1
        self.current_column = 4
        self.current_tile = 1
        self.my_tile_path = []
        self.correct_tile_path = []
        self.move_speed = 4
        self.animation_frame = 1
        self.animation_count_run = 0.25
        self.animation_count_stand = 0.1
        self.run_frames_up = True
        self.current_dir = "stand_down"  # je nach Bewegungsrichtung aendert sich die current_dir
        self.load_rect()
        self.key_pressed = False
        self.arrived = False # sobald arrived=True ist der Spieler am Ziel angekommen, wird bei movement() umgestellt
        self.spawned = False
        self.offset = pygame.math.Vector2(0, 0)

    def track_tile_path(self):
        if self.current_tile not in self.my_tile_path:
            self.my_tile_path.append(self.current_tile)

    def player_input(self):

        def run_up():
            if (self.current_row == 8 and self.current_tile == 47) or self.current_row < 8:
                self.current_dir = "run_up"
                self.key_pressed = True

        def run_left():
            if self.current_tile != 2 and self.current_tile != 9 and self.current_tile != 16 and \
                    self.current_tile != 23 and self.current_tile != 30 and self.current_tile != 37 and \
                    self.current_tile != 44 and self.current_tile != 1 and self.current_tile != 51:
                self.current_dir = "run_left"
                self.key_pressed = True

        def run_right():
            if self.current_tile != 8 and self.current_tile != 15 and self.current_tile != 22 and \
                    self.current_tile != 29 and self.current_tile != 36 and self.current_tile != 43 and \
                    self.current_tile != 50 and self.current_tile != 1 and self.current_tile != 51:
                self.current_dir = "run_right"
                self.key_pressed = True

        self.keys = pygame.key.get_pressed()
        if self.arrived != True:
            # player 1: w a d
            if self.pnum == 1:
                if self.key_pressed != True:
                    # W -> UP
                    if self.keys[pygame.K_w]:
                        run_up()
                    # A -> LEFT
                    elif self.keys[pygame.K_a]:
                        run_left()
                    # D -> RIGHT
                    elif self.keys[pygame.K_d]:
                        run_right()
            # player 1: i j k
            elif self.pnum == 2:
                if self.key_pressed != True:
                    # I -> UP
                    if self.keys[pygame.K_i]:
                        run_up()
                    # J -> LEFT
                    elif self.keys[pygame.K_j]:
                        run_left()
                    # K -> RIGHT
                    elif self.keys[pygame.K_k]:
                        run_right()

    def movement(self):

        def check_row(row):
            if self.current_row == row:
                if self.rect.bottom - self.move_speed <= (borders[row]["upper"] - (((borders[row]["upper"] - borders[row+1]["upper"])//3) if self.current_row < 9 else 0)):
                    self.current_row += 1
                    self.key_pressed = False
                    self.current_dir = "stand_up"
                    if self.current_tile != 51:
                        if self.current_tile == 1:
                            self.current_tile = 5
                        elif self.current_tile == 47:
                            self.current_tile = 51
                        else:
                            self.current_tile += 7
                if self.current_row >= 5:
                    self.move_speed = 3

        def check_tile(direct):
            if direct == "left":
                if self.rect.right - self.move_speed <= (borders[self.current_row][f"tile_{self.current_tile - 1}"] -
                ((borders[self.current_row][f"tile_{self.current_tile}"] - borders[self.current_row][f"tile_{self.current_tile - 1}"])//3)):
                    self.current_tile -= 1
                    self.key_pressed = False
                    self.current_dir = "stand_left"
            elif direct == "right":
                if self.rect.left + self.move_speed >= (borders[self.current_row][f"tile_{self.current_tile}"] +
                ((borders[self.current_row][f"tile_{self.current_tile + 1}"] - borders[self.current_row][f"tile_{self.current_tile}"])//3)):
                    self.current_tile += 1
                    self.key_pressed = False
                    self.current_dir = "stand_right"

        self.check_current_column()

        if self.key_pressed:
            if "_up" in self.current_dir:
                for i in range(9):
                    check_row(i+1)
                self.y -= self.move_speed

                match self.current_column:
                    case 1:
                        self.x += 1.2 if self.current_row < 6 else 1.1
                    case 2:
                        self.x += 0.9 if self.current_row < 6 else 0.8
                    case 3:
                        self.x += 0.6 if self.current_row < 6 else 0.5
                    case 5:
                        self.x -= 0.6 if self.current_row < 6 else 0.5
                    case 6:
                        self.x -= 0.9 if self.current_row < 6 else 0.8
                    case 7:
                        self.x -= 1.2 if self.current_row < 6 else 1.1

                if self.current_row == 10:
                    self.arrived = True
            elif "_left" in self.current_dir:
                check_tile("left")
                self.x -= self.move_speed
            elif "_right" in self.current_dir:
                check_tile("right")
                self.x += self.move_speed
        self.pos = (self.x, self.y)

    def spawn_to(self, tile_no:int):

        def return_row(tile:int) -> int:
            if tile < 9:
                return 2
            elif tile < 16:
                return 3
            elif tile < 23:
                return 4
            elif tile < 30:
                return 5
            elif tile < 37:
                return 6
            elif tile < 44:
                return 7
            else:
                return 8

        def spawn_animation():
            self.spawned = True
            self.x += self.current_sprites[1].get_width() // 3
            for frame in self.current_sprites.keys():
                self.current_sprites[frame] = pygame.transform.scale(self.current_sprites[frame], (self.current_sprites[frame].get_width() // 3, self.current_sprites[frame].get_height()))
            self.draw()
            self.spawned = False

        spawn_animation()

        row = return_row(tile_no)

        self.y = (borders[row]["upper"] + ((borders[row - 1]["upper"] - borders[row]["upper"]) // 2)) - (self.current_sprites[round(self.animation_frame)].get_height())

        if tile_no == 2 or tile_no == 9 or tile_no == 16 or tile_no == 23 or tile_no == 30 or tile_no == 37 or tile_no == 44:
            self.x = (borders[row][f"tile_{tile_no}"] - (((borders[row][f"tile_{tile_no + 1}"] - borders[row][f"tile_{tile_no}"]) // 3) * 2))
        else:
            self.x = (borders[row][f"tile_{tile_no - 1}"] + ((borders[row][f"tile_{tile_no}"] - borders[row][f"tile_{tile_no - 1}"]) // 6))

        self.current_row = row
        self.current_tile = tile_no
        self.pos = (self.x, self.y)


    def check_if_correct_path(self):
        ind_to_check = len(self.my_tile_path) - 1
        if self.my_tile_path[ind_to_check] != self.correct_tile_path[ind_to_check]:
            self.my_tile_path.pop() # remove the last list item (here the incorrect tile)
            self.spawn_to(self.my_tile_path[-1]) # spawn to last correct tile

    def update(self):
        self.track_tile_path()
        self.check_if_correct_path()
        self.load_rect()
        self.player_input()
        self.movement()
        self.draw()
        # print(self.x)
        # print(self.y)
        # print("ROW", self.current_row)
        # print("TILE", self.current_tile)
        # print("COLUMN", self.current_column)
