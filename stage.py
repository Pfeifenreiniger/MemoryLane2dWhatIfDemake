
from main import pygame, SCREEN, random


class Stage:
    def __init__(self):
        self.load_elements()
        self.correct_tiles = []
        self.draw_elements()

    def load_elements(self):
        # load-sub-methods for loading graphic assets with xy-positions
        def load_bg():
            self.bg = pygame.image.load("graphics/stage/bg/background.png").convert_alpha()
            self.bg_pos = (0, 0)

        def load_chains():
            # left chains
            # graphics
            self.chains_left = []
            for i in range(5):
                self.chains_left.append(
                    pygame.image.load(f"graphics/stage/chains/left/chainsL0{i + 1}.png").convert_alpha())

            # xy-positions
            self.chains_left_pos = [[-14, -8], [-17, 217], [-29, 346], [174, -5], [85, -13]]

            # right chains
            # graphics
            self.chains_right = []
            for i in range(5):
                self.chains_right.append(
                    pygame.image.load(f"graphics/stage/chains/right/chainsR0{i + 1}.png").convert_alpha())

            # xy-positions
            self.chains_right_pos = [[583, -5], [636, 220], [691, 348], [502, -2], [530, -10]]

            self.rotate_angles = []
            for i in range(5):
                self.rotate_angles.append(random.randint(-2, 2))

            self.swing = True

        def load_neon_signs():
            # key = frame : value = image

            # left signs

            self.bullet_bills = {
                1: pygame.image.load("graphics/stage/neon_signs/left/bullet_bills/bullet_bills_f1.png").convert_alpha(),
                2: pygame.image.load("graphics/stage/neon_signs/left/bullet_bills/bullet_bills_f2.png").convert_alpha()
            }

            self.bullet_bills_pos = (-16, 243)

            self.vote_for_koopa = {
                1: pygame.image.load(
                    "graphics/stage/neon_signs/left/vote_for_koopa/vote_for_koopa_f1.png").convert_alpha(),
                2: pygame.image.load(
                    "graphics/stage/neon_signs/left/vote_for_koopa/vote_for_koopa_f2.png").convert_alpha()
            }

            self.vote_for_koopa_pos = (126, 68)

            # right signs

            self.fire_snake = {
                1: pygame.image.load("graphics/stage/neon_signs/right/fire_snake/fire_snake_f1.png").convert_alpha(),
                2: pygame.image.load("graphics/stage/neon_signs/right/fire_snake/fire_snake_f2.png").convert_alpha()
            }

            self.fire_snake_pos = (532, 284)

            self.parts_frame = 1
            self.parts = {
                1: pygame.image.load("graphics/stage/neon_signs/right/parts/parts_f1.png").convert_alpha(),
                2: pygame.image.load("graphics/stage/neon_signs/right/parts/parts_f2.png").convert_alpha()
            }

            self.parts_pos = (585, 5)

        def load_piranha_plants():
            # key = frame : value = image

            # left plant

            self.piranha_plant_frame_left = 1
            self.piranha_plant_left_frames_forwards = True
            self.piranha_plant_left = {}

            for i in range(3):
                self.piranha_plant_left.update({i + 1: pygame.image.load(
                    f"graphics/stage/piranha_plants/left/piranha_plant_left_f{i + 1}.png").convert_alpha()})

            self.piranha_plant_left_pos = (32, -18)

            # right plant

            self.piranha_plant_frame_right = 2
            self.piranha_plant_right_frames_forwards = True
            self.piranha_plant_right = {}

            for i in range(3):
                self.piranha_plant_right.update({i + 1: pygame.image.load(
                    f"graphics/stage/piranha_plants/right/piranha_plant_right_f{i + 1}.png").convert_alpha()})

            self.piranha_plant_right_pos = (577, -44)

        def load_tiles():
            # key = tile no : value = image

            def load_tiles_loop(tiles_dict : dict, tiles_folder : str):
                for i in range(51):
                    tiles_dict.update({i + 1: pygame.image.load(
                        f"graphics/stage/tiles/{tiles_folder}/tile{'0' + str(i + 1) if (i + 1) < 10 else i + 1}.png").convert_alpha()})
                return tiles_dict

            self.tiles_f1 = {}
            self.tiles_f2 = {}
            self.tiles_f3 = {}
            self.tiles_f4 = {}
            self.tiles_corr = {}

            self.tiles_f1 = load_tiles_loop(self.tiles_f1, "f1")
            self.tiles_f2 = load_tiles_loop(self.tiles_f2, "f2")
            self.tiles_f3 = load_tiles_loop(self.tiles_f3, "f3")
            self.tiles_f4 = load_tiles_loop(self.tiles_f4, "f4")
            self.tiles_frames = [self.tiles_f1, self.tiles_f2, self.tiles_f3, self.tiles_f4]
            self.tiles_frames_no = 0
            self.tiles_frames_forwards = True
            self.tiles_corr = load_tiles_loop(self.tiles_corr, "corr")

            self.tiles_pos = {
                1 : (346, 504),
                2 : (65, 434),
                3 : (166, 434),
                4 : (259, 434),
                5 : (351, 434),
                6 : (443, 434),
                7 : (530, 434),
                8 : (616, 434),
                9 : (94, 377),
                10 : (183, 377),
                11 : (268, 377),
                12 : (355, 377),
                13 : (440, 377),
                14 : (520, 377),
                15 : (598, 377),
                16 : (117, 327),
                17 : (198, 327),
                18 : (279, 327),
                19 : (359, 327),
                20 : (436, 327),
                21 : (511, 327),
                22 : (584, 327),
                23 : (137, 285),
                24 : (212, 285),
                25 : (288, 285),
                26 : (361, 285),
                27 : (433, 285),
                28 : (503, 285),
                29 : (572, 285),
                30 : (155, 247),
                31 : (225, 247),
                32 : (294, 247),
                33 : (364, 247),
                34 : (431, 247),
                35 : (496, 247),
                36 : (561, 247),
                37 : (172, 213),
                38 : (236, 213),
                39 : (300, 213),
                40 : (365, 213),
                41 : (429, 213),
                42 : (491, 213),
                43 : (551, 213),
                44 : (185, 184),
                45 : (246, 184),
                46 : (306, 184),
                47 : (367, 184),
                48 : (428, 184),
                49 : (486, 184),
                50 : (544, 184),
                51 : (368, 158)
            }

            self.stepping_stone = pygame.image.load("graphics/stage/tiles/steppingStone.png").convert_alpha()

            self.stepping_stone_pos = (344, 583)

        def load_tower():
            # key = frame : value = image

            self.tower = {
                1: pygame.image.load("graphics/stage/tower/tower_f1.png").convert_alpha(),
                2: pygame.image.load("graphics/stage/tower/tower_f2.png").convert_alpha()
            }

            self.tower_pos = (189, -9)

        def load_trails():
            self.trails = pygame.image.load("graphics/stage/trails/trails.png").convert_alpha()

            self.trails_pos = (150, 381)

        # call of sub-methods for loading graphic assets
        load_bg()
        load_chains()
        load_neon_signs()
        load_piranha_plants()
        load_tiles()
        load_tower()
        load_trails()

    def draw_elements(self):
        def draw_bg():
            SCREEN.blit(self.bg, self.bg_pos)

        def draw_trails():
            SCREEN.blit(self.trails, self.trails_pos)

        def draw_neon_signs():
            # left signs
            SCREEN.blit(self.bullet_bills[2 if random.randint(1, 100) <= 2 else 1], self.bullet_bills_pos)

            SCREEN.blit(self.vote_for_koopa[2 if random.randint(1, 100) <= 2 else 1], self.vote_for_koopa_pos)

            # right signs
            SCREEN.blit(self.fire_snake[2 if random.randint(1, 100) <= 2 else 1], self.fire_snake_pos)

            if round(self.parts_frame + 0.05) > 2:
                self.parts_frame = 1
            else: self.parts_frame += 0.05
            SCREEN.blit(self.parts[round(self.parts_frame)], self.parts_pos)

        def draw_chains():
            for i in range(5):
                rotated_img_left = pygame.transform.rotate(self.chains_left[i], round(self.rotate_angles[i]))
                rotated_rect_left = rotated_img_left.get_rect(center = self.chains_left[i].get_rect(topleft = self.chains_left_pos[i]).center)
                SCREEN.blit(rotated_img_left, rotated_rect_left)

                rotated_img_right = pygame.transform.rotate(self.chains_right[i], round(self.rotate_angles[i]))
                rotated_rect_right = rotated_img_right.get_rect(center = self.chains_right[i].get_rect(topleft = self.chains_right_pos[i]).center)
                SCREEN.blit(rotated_img_right, rotated_rect_right)

                if self.rotate_angles[i] > 2:
                    self.swing = False
                elif self.rotate_angles[i] < -2:
                    self.swing = True

                if self.swing:
                    self.rotate_angles[i] += 0.08
                else:
                    self.rotate_angles[i] -= 0.08

        def draw_tower():
            SCREEN.blit(self.tower[2 if random.randint(1, 100) <= 3 else 1], self.tower_pos)

        def draw_piranha_plants():
            # plant left
            if self.piranha_plant_left_frames_forwards:
                if round(self.piranha_plant_frame_left + 0.1) > 3:
                    self.piranha_plant_left_frames_forwards = False
                else: self.piranha_plant_frame_left += 0.1
            else:
                if round(self.piranha_plant_frame_left - 0.1) < 1:
                    self.piranha_plant_left_frames_forwards = True
                else: self.piranha_plant_frame_left -= 0.1

            SCREEN.blit(self.piranha_plant_left[round(self.piranha_plant_frame_left)], self.piranha_plant_left_pos)

            # plant right
            if self.piranha_plant_right_frames_forwards:
                if round(self.piranha_plant_frame_right + 0.1) > 3:
                    self.piranha_plant_right_frames_forwards = False
                else: self.piranha_plant_frame_right += 0.1
            else:
                if round(self.piranha_plant_frame_right - 0.1) < 1:
                    self.piranha_plant_right_frames_forwards = True
                else: self.piranha_plant_frame_right -= 0.1

            SCREEN.blit(self.piranha_plant_right[round(self.piranha_plant_frame_right)], self.piranha_plant_right_pos)

        def draw_tiles():

            SCREEN.blit(self.stepping_stone, self.stepping_stone_pos)

            if self.tiles_frames_forwards:
                if round(self.tiles_frames_no + 0.06) > 3:
                    self.tiles_frames_forwards = False
                else: self.tiles_frames_no += 0.06
            else:
                if round(self.tiles_frames_no - 0.06) < 0:
                    self.tiles_frames_forwards = True
                else: self.tiles_frames_no -= 0.06

            for no, tile in self.tiles_frames[round(self.tiles_frames_no)].items():
                SCREEN.blit(tile, self.tiles_pos[no])

            if len(self.correct_tiles) > 0:
                for tile in self.correct_tiles:
                    SCREEN.blit(self.tiles_corr[tile], self.tiles_pos[tile])

        draw_bg()
        draw_trails()
        draw_neon_signs()
        draw_chains()
        draw_tower()
        draw_piranha_plants()
        draw_tiles()

    def get_correct_tiles(self, correct_tiles: list):
        if len(correct_tiles) > 0:
            for tile in correct_tiles:
                if tile not in self.correct_tiles:
                    self.correct_tiles.append(tile)


from tiles_field_borders import *

class ShyGuy:

    def __init__(self):
        self.sprites = self.load_sprites()
        self.x = 365
        self.y = 520
        self.move_speed = 4
        self.animation_frame = 1
        self.animation_count_run = 0.25
        self.animation_count_stand = 0.1
        self.run_frames_up = True
        self.current_dir = "stand_down" # je nach Bewegungsrichtung aendert sich die current_dir
        self.current_tile = 1
        self.current_row = 1
        self.row_1_to_2 = False
        self.row_2_to_3 = False
        self.row_3_to_4 = False
        self.row_4_to_5 = False
        self.row_5_to_6 = False
        self.row_6_to_7 = False
        self.row_7_to_8 = False
        self.row_8_to_9 = False
        self.current_column = 1
        self.load_rect()
        self.path = self.calculate_path()
        self.my_path = []
        self.scaled = False

    def load_rect(self):
        self.rect = pygame.rect.Rect((
                self.x + (self.sprites[self.current_dir][round(self.animation_frame)].get_width() / 3)), # x pos
                self.y + (self.sprites[self.current_dir][round(self.animation_frame)].get_height() / 1.2), # y pos
                (self.sprites[self.current_dir][round(self.animation_frame)].get_width() / 3), # width
                (self.sprites[self.current_dir][round(self.animation_frame)].get_height() / 5)) # height

    def load_sprites(self) -> dict:

        run_left = {}

        run_right = {}

        run_up = {}

        stand_down = {}

        stand_left = {}

        stand_right = {}

        stand_up = {}

        shy_sprites = {
            "run_left" : run_left,
            "run_right" : run_right,
            "run_up" : run_up,
            "stand_down" : stand_down,
            "stand_left" : stand_left,
            "stand_right" : stand_right,
            "stand_up" : stand_up,
            "shadow" : pygame.image.load("graphics/shadow.png").convert_alpha()
        }

        shy_sprites["shadow"].set_alpha(128)

        # dir for file directory
        for dir in shy_sprites.keys():
            if not dir.startswith("shadow"):
                if dir.startswith("run_"):
                    j = 4
                else:
                    j = 2

                for i in range(j):
                    img = pygame.image.load(f"graphics/stage/shy/{dir}/shy_{dir}_f{i+1}.png").convert_alpha()
                    shy_sprites[dir][i+1] = img

        return shy_sprites

    def animation(self):
        if self.current_dir.startswith("run_"):
            if self.run_frames_up:
                if round(self.animation_frame + self.animation_count_run) > 4:
                    self.run_frames_up = False
                else: self.animation_frame += self.animation_count_run
            else:
                if round(self.animation_frame - self.animation_count_run) < 1:
                    self.run_frames_up = True
                else: self.animation_frame -= self.animation_count_run
        else:
            if round(self.animation_frame + self.animation_count_stand) > 2:
                self.animation_frame = 1
            else: self.animation_frame += self.animation_count_stand

    def draw_sprites(self):

        self.animation()

        # draw shadow
        SCREEN.blit(self.sprites["shadow"], (self.rect.left - (self.sprites[self.current_dir][round(self.animation_frame)].get_width() / 4),
                                             self.rect.top + (self.sprites[self.current_dir][round(self.animation_frame)].get_height() / 12)))

        # scale
        if self.scaled != True:
            self.scaled = True

            # run sprites
            runs = ["run_left", "run_right", "run_up"]
            for i in range(4):
                for run in runs:
                    self.sprites[run][i+1] = pygame.transform.scale(self.sprites[run][i+1], (self.sprites[run][i+1].get_width() - 1.2, self.sprites[run][i+1].get_height() - 1.2))

            # stand sprites
            stands = ["stand_left", "stand_right", "stand_up", "stand_down"]
            for i in range(2):
                for stand in stands:
                    self.sprites[stand][i + 1] = pygame.transform.scale(self.sprites[stand][i + 1], (self.sprites[stand][i + 1].get_width() - 1.2, self.sprites[stand][i + 1].get_height() - 1.2))

            self.sprites["shadow"] = pygame.transform.smoothscale(self.sprites["shadow"], (self.sprites["shadow"].get_width() - 2, self.sprites["shadow"].get_height() - 2))

        # draw current shyguy sprite
        SCREEN.blit(self.sprites[self.current_dir][round(self.animation_frame)], (self.x, self.y))

        # pygame.draw.rect(SCREEN, (000, 000, 000), self.rect)

    def calculate_path(self) -> dict:

        # key = row no, value = walk to this tile no horizontally
        path = {
            1 : 1,
            2 : random.randint(2, 8),
            3 : random.randint(9, 15),
            4 : random.randint(16, 22),
            5 : random.randint(23, 29),
            6 : random.randint(30, 36),
            7 : random.randint(37, 43),
            8 : 47,
            9 : 51
        }

        return path

    def record_my_path(self, tile: int):

        if tile not in self.my_path:
            self.my_path.append(tile)

    def check_current_row(self):

        def calc_diff_vertically(current_row: int, next_row: int) -> int:
            return round(abs(borders[next_row]["upper"] - borders[current_row]["upper"]))

        def switch_tile():
            if self.current_row > 1 and self.current_row < 8:
                self.current_tile = self.current_tile + 7
            elif self.current_row == 1:
                self.current_tile = 5
            else:
                self.current_tile = 51

        if self.rect.bottom < (borders[8]["upper"] - (calc_diff_vertically(8, 9) / 2)) and self.row_8_to_9 != True:
            switch_tile()
            self.current_row = 9
            self.scaled = False
            self.row_8_to_9 = True
        elif self.rect.bottom < (borders[7]["upper"] - (calc_diff_vertically(7, 8) / 3)) and self.row_7_to_8 != True:
            switch_tile()
            self.current_row = 8
            self.scaled = False
            self.row_7_to_8 = True
        elif self.rect.bottom < (borders[6]["upper"] - (calc_diff_vertically(6, 7) / 4)) and self.row_6_to_7 != True:
            switch_tile()
            self.current_row = 7
            self.scaled = False
            self.row_6_to_7 = True
        elif self.rect.bottom < (borders[5]["upper"] - (calc_diff_vertically(5, 6) / 4)) and self.row_5_to_6 != True:
            switch_tile()
            self.current_row = 6
            self.scaled = False
            self.row_5_to_6 = True
        elif self.rect.bottom < (borders[4]["upper"] - (calc_diff_vertically(4, 5) / 4)) and self.row_4_to_5 != True:
            switch_tile()
            self.current_row = 5
            self.scaled = False
            self.row_4_to_5 = True
        elif self.rect.bottom < (borders[3]["upper"] - (calc_diff_vertically(3, 4) / 4)) and self.row_3_to_4 != True:
            switch_tile()
            self.current_row = 4
            self.scaled = False
            self.row_3_to_4 = True
        elif self.rect.bottom < (borders[2]["upper"] - (calc_diff_vertically(2, 3) / 4)) and self.row_2_to_3 != True:
            switch_tile()
            self.current_row = 3
            self.scaled = False
            self.row_2_to_3 = True
        elif self.rect.bottom < (borders[1]["upper"] - (calc_diff_vertically(1, 2) / 4)) and self.row_1_to_2 != True:
            switch_tile()
            self.current_row = 2
            self.scaled = False
            self.row_1_to_2 = True

    def check_current_column(self):
        if self.current_tile == 2 or self.current_tile == 9 or self.current_tile == 16 or self.current_tile == 23\
                or self.current_tile == 30 or self.current_tile == 37 or self.current_tile == 44:
            self.current_column = 1
        elif self.current_tile == 3 or self.current_tile == 10 or self.current_tile == 17 or self.current_tile == 24\
                or self.current_tile == 31 or self.current_tile == 38 or self.current_tile == 45:
            self.current_column = 2
        elif self.current_tile == 4 or self.current_tile == 11 or self.current_tile == 18 or self.current_tile == 25 \
                or self.current_tile == 32 or self.current_tile == 39 or self.current_tile == 46:
            self.current_column = 3
        elif self.current_tile == 5 or self.current_tile == 12 or self.current_tile == 19 or self.current_tile == 26 \
                or self.current_tile == 33 or self.current_tile == 40 or self.current_tile == 47 or self.current_tile == 51:
            self.current_column = 4
        elif self.current_tile == 6 or self.current_tile == 13 or self.current_tile == 20 or self.current_tile == 27 \
                or self.current_tile == 34 or self.current_tile == 41 or self.current_tile == 48:
            self.current_column = 5
        elif self.current_tile == 7 or self.current_tile == 14 or self.current_tile == 21 or self.current_tile == 28 \
                or self.current_tile == 35 or self.current_tile == 42 or self.current_tile == 49:
            self.current_column = 6
        elif self.current_tile == 8 or self.current_tile == 15 or self.current_tile == 22 or self.current_tile == 29 \
                or self.current_tile == 36 or self.current_tile == 43 or self.current_tile == 50:
            self.current_column = 7

    def check_current_tile(self):

        def calc_diff_horizontally(tile : int, next_tile: int) -> int:
            try:
                return round(abs(borders[self.current_row][f"tile_{next_tile}"] - borders[self.current_row][f"tile_{tile}"]))
            except KeyError:
                return 0

        from_number = 0
        to_number = 0

        if not self.current_dir.endswith("_up"):

            if self.current_row == 2:
                from_number = 2
                to_number = 8
            elif self.current_row == 3:
                from_number = 9
                to_number = 15
            elif self.current_row == 4:
                from_number = 16
                to_number = 22
            elif self.current_row == 5:
                from_number = 23
                to_number = 29
            elif self.current_row == 6:
                from_number = 30
                to_number = 36
            elif self.current_row == 7:
                from_number = 37
                to_number = 43
            elif self.current_row == 8:
                from_number = 44
                to_number = 50
            elif self.current_row == 9:
                self.current_tile = 51

            if self.current_row != 9 and self.current_row != 1:
                for tile in range(from_number, to_number):
                    # runs right
                    if self.current_dir.endswith("_right") and self.current_tile != to_number:
                        if self.rect.left > (borders[self.current_row][f"tile_{to_number-1}"] + (calc_diff_horizontally(to_number-1, to_number) / 4)):
                            self.current_tile = to_number
                            break
                        elif self.rect.left < (borders[self.current_row][f"tile_{tile}"] + (calc_diff_horizontally(tile, tile+1) / 4)):
                            self.current_tile = tile
                            break
                    # runs left
                    if self.current_dir.endswith("_left") and self.current_tile != from_number:
                        if self.rect.right < (borders[self.current_row][f"tile_{from_number}"] - (calc_diff_horizontally(from_number, from_number+1) / 4)):
                            self.current_tile = from_number
                            break
                        if self.current_tile != from_number + 1:
                            if self.rect.right < (borders[self.current_row][f"tile_{tile}"] - (calc_diff_horizontally(tile, tile-1) / 4)):
                                self.current_tile = tile
                                break


    def move(self):

        def move_up(column: int = 4):
            self.current_dir = "run_up"
            self.y -= self.move_speed

            match column:
                case 1: self.x += 0.8 if self.current_row < 6 else 0.7
                case 2: self.x += 0.7 if self.current_row < 6 else 0.6
                case 3: self.x += 0.6 if self.current_row < 6 else 0.5
                case 5: self.x -= 0.6 if self.current_row < 6 else 0.5
                case 6: self.x -= 0.7 if self.current_row < 6 else 0.6
                case 7: self.x -= 0.8 if self.current_row < 6 else 0.7

        def move_right():
            self.current_dir = "run_right"
            self.x += self.move_speed

        def move_left():
            self.current_dir = "run_left"
            self.x -= self.move_speed

        if self.current_row > 5:
            self.move_speed = 3
            self.animation_count_run = 0.2

        self.check_current_row()
        self.check_current_column()
        self.check_current_tile()

        if self.current_row == 1:
            move_up()
        elif self.current_row == 9:
            self.current_dir = "stand_down"
        else:
            for i in range(2, 9):
                if i == self.current_row:
                    if self.current_tile == self.path[i]:
                        move_up(self.current_column)
                    else:
                        if self.current_tile < self.path[i]:
                            move_right()
                        else:
                            move_left()

    def update(self):
        self.load_rect()
        self.move()
        self.record_my_path(self.current_tile)
        self.draw_sprites()

