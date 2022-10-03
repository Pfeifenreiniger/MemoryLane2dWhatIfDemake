
from main import pygame, SCREEN, random


class Stage:
    def __init__(self, pnum, canvas):
        self.pnum = pnum # 0 for full-screen, 1 to 4 for the split-screens
        self.canvas = canvas
        if self.pnum == 1:
            self.offset = pygame.math.Vector2(200, 300)
            self.surf_area = pygame.Rect(0,0,400,300)
            self.sub_canvas = self.canvas.subsurface(self.surf_area)
        elif self.pnum == 2:
            self.offset = pygame.math.Vector2(200, 300)
            self.surf_area = pygame.Rect(400,0,400,300)
            self.sub_canvas = self.canvas.subsurface(self.surf_area)
        else:
            self.offset = pygame.math.Vector2(0, 0)
        self.load_elements()
        self.correct_tiles = []

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
            bg_offset = self.bg_pos - self.offset
            if self.pnum != 0:
                self.sub_canvas.blit(self.bg, bg_offset)
            else:
                SCREEN.blit(self.bg, bg_offset)

        def draw_trails():
            trails_offset = self.trails_pos - self.offset
            if self.pnum != 0:
                self.sub_canvas.blit(self.trails, trails_offset)
            else:
                SCREEN.blit(self.trails, trails_offset)

        def draw_neon_signs():
            # left signs
            bullet_bills_offset = self.bullet_bills_pos - self.offset
            if self.pnum != 0:
                self.sub_canvas.blit(self.bullet_bills[2 if random.randint(1, 100) <= 2 else 1], bullet_bills_offset)
            else:
                SCREEN.blit(self.bullet_bills[2 if random.randint(1, 100) <= 2 else 1], bullet_bills_offset)

            vote_for_koopa_offset = self.vote_for_koopa_pos - self.offset
            if self.pnum != 0:
                self.sub_canvas.blit(self.vote_for_koopa[2 if random.randint(1, 100) <= 2 else 1], vote_for_koopa_offset)
            else:
                SCREEN.blit(self.vote_for_koopa[2 if random.randint(1, 100) <= 2 else 1], vote_for_koopa_offset)

            # right signs
            fire_snake_offset = self.fire_snake_pos - self.offset
            if self.pnum != 0:
                self.sub_canvas.blit(self.fire_snake[2 if random.randint(1, 100) <= 2 else 1], fire_snake_offset)
            else:
                SCREEN.blit(self.fire_snake[2 if random.randint(1, 100) <= 2 else 1], fire_snake_offset)

            if round(self.parts_frame + 0.05) > 2:
                self.parts_frame = 1
            else: self.parts_frame += 0.05
            parts_offset = self.parts_pos - self.offset
            if self.pnum != 0:
                self.sub_canvas.blit(self.parts[round(self.parts_frame)], parts_offset)
            else:
                SCREEN.blit(self.parts[round(self.parts_frame)], parts_offset)

        def draw_chains():
            for i in range(5):
                rotated_img_left = pygame.transform.rotate(self.chains_left[i], round(self.rotate_angles[i]))
                rotated_rect_left = rotated_img_left.get_rect(center = self.chains_left[i].get_rect(topleft = self.chains_left_pos[i]).center)
                rotated_left_offset = rotated_rect_left.topleft - self.offset
                if self.pnum != 0:
                    self.sub_canvas.blit(rotated_img_left, rotated_left_offset)
                else:
                    SCREEN.blit(rotated_img_left, rotated_left_offset)

                rotated_img_right = pygame.transform.rotate(self.chains_right[i], round(self.rotate_angles[i]))
                rotated_rect_right = rotated_img_right.get_rect(center = self.chains_right[i].get_rect(topleft = self.chains_right_pos[i]).center)
                rotated_right_offset = rotated_rect_right.topleft - self.offset
                if self.pnum != 0:
                    self.sub_canvas.blit(rotated_img_right, rotated_right_offset)
                else:
                    SCREEN.blit(rotated_img_right, rotated_right_offset)

                if self.rotate_angles[i] > 2:
                    self.swing = False
                elif self.rotate_angles[i] < -2:
                    self.swing = True

                if self.swing:
                    self.rotate_angles[i] += 0.08
                else:
                    self.rotate_angles[i] -= 0.08

        def draw_tower():
            tower_offset = self.tower_pos - self.offset
            if self.pnum != 0:
                self.sub_canvas.blit(self.tower[2 if random.randint(1, 100) <= 3 else 1], tower_offset)
            else:
                SCREEN.blit(self.tower[2 if random.randint(1, 100) <= 3 else 1], tower_offset)

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

            piranha_plant_left_offset = self.piranha_plant_left_pos - self.offset
            if self.pnum != 0:
                self.sub_canvas.blit(self.piranha_plant_left[round(self.piranha_plant_frame_left)], piranha_plant_left_offset)
            else:
                SCREEN.blit(self.piranha_plant_left[round(self.piranha_plant_frame_left)], piranha_plant_left_offset)

            # plant right
            if self.piranha_plant_right_frames_forwards:
                if round(self.piranha_plant_frame_right + 0.1) > 3:
                    self.piranha_plant_right_frames_forwards = False
                else: self.piranha_plant_frame_right += 0.1
            else:
                if round(self.piranha_plant_frame_right - 0.1) < 1:
                    self.piranha_plant_right_frames_forwards = True
                else: self.piranha_plant_frame_right -= 0.1

            piranha_plant_right_offset = self.piranha_plant_right_pos - self.offset
            if self.pnum != 0:
                self.sub_canvas.blit(self.piranha_plant_right[round(self.piranha_plant_frame_right)], piranha_plant_right_offset)
            else:
                SCREEN.blit(self.piranha_plant_right[round(self.piranha_plant_frame_right)], piranha_plant_right_offset)

        def draw_tiles():

            stepping_stone_offset = self.stepping_stone_pos - self.offset
            if self.pnum != 0:
                self.sub_canvas.blit(self.stepping_stone, stepping_stone_offset)
            else:
                SCREEN.blit(self.stepping_stone, stepping_stone_offset)

            if self.tiles_frames_forwards:
                if round(self.tiles_frames_no + 0.06) > 3:
                    self.tiles_frames_forwards = False
                else: self.tiles_frames_no += 0.06
            else:
                if round(self.tiles_frames_no - 0.06) < 0:
                    self.tiles_frames_forwards = True
                else: self.tiles_frames_no -= 0.06

            for no, tile in self.tiles_frames[round(self.tiles_frames_no)].items():
                tile_offset = self.tiles_pos[no] - self.offset
                if self.pnum != 0:
                    self.sub_canvas.blit(tile, tile_offset)
                else:
                    SCREEN.blit(tile, tile_offset)

            if len(self.correct_tiles) > 0:
                for tile in self.correct_tiles:
                    tile_offset = self.tiles_pos[tile] - self.offset
                    if self.pnum != 0:
                        self.sub_canvas.blit(self.tiles_corr[tile], tile_offset)
                    else:
                        SCREEN.blit(self.tiles_corr[tile], tile_offset)

        if self.pnum != 0:
            SCREEN.blit(self.sub_canvas, self.surf_area)

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
        self.sprites = self.load_sprites("graphics/stage", "shy")
        self.x = 365
        self.y = 520
        self.pos = (self.x, self.y)
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
        self.spawned = False
        self.pnum = 0
        self.offset = pygame.math.Vector2(0, 0)

    def load_rect(self):
        self.rect = pygame.rect.Rect((
                self.x + (self.sprites[self.current_dir][round(self.animation_frame)].get_width() / 3)), # x pos
                self.y + (self.sprites[self.current_dir][round(self.animation_frame)].get_height() / 1.2), # y pos
                (self.sprites[self.current_dir][round(self.animation_frame)].get_width() / 3), # width
                (self.sprites[self.current_dir][round(self.animation_frame)].get_height() / 5)) # height

    def load_sprites(self, file_direct:str, char:str) -> dict:

        run_left = {}

        run_right = {}

        run_up = {}

        stand_down = {}

        stand_left = {}

        stand_right = {}

        stand_up = {}

        sprites = {
            "run_left" : run_left,
            "run_right" : run_right,
            "run_up" : run_up,
            "stand_down" : stand_down,
            "stand_left" : stand_left,
            "stand_right" : stand_right,
            "stand_up" : stand_up,
            "shadow" : pygame.image.load("graphics/shadow.png").convert_alpha()
        }

        sprites["shadow"].set_alpha(128)

        # dir for file directory
        for dir in sprites.keys():
            if not dir.startswith("shadow"):
                if dir.startswith("run_"):
                    j = 4
                else:
                    j = 2

                for i in range(j):
                    img = pygame.image.load(f"{file_direct}/{char}/{dir}/{char}_{dir}_f{i+1}.png").convert_alpha()
                    sprites[dir][i+1] = img

        return sprites

    def get_current_sprites(self) -> dict:

        size_diff = round((self.current_row - 1) * 1.2, 1)
        copy_sprites_dict = self.sprites[self.current_dir].copy()
        for frame, sprite in self.sprites[self.current_dir].items():
            copy_sprites_dict[frame] = pygame.transform.scale(sprite, (68 - size_diff, 75 - size_diff))
        copy_sprites_dict['shadow'] = pygame.transform.scale(self.sprites['shadow'], (68 - size_diff, 25 - size_diff))
        return copy_sprites_dict

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

    def draw(self):
        self.animation()

        if self.spawned != True:
            self.current_sprites = self.get_current_sprites()

        offset = [0, 0]
        if self.pnum == 1:
            offset = self.pos - self.offset
        elif self.pnum == 2:
            offset[0] = self.pos[0] + self.offset[0] # x
            offset[1] = self.pos[1] - self.offset[1] # y

        # draw shadow
        SCREEN.blit(self.current_sprites["shadow"], (offset[0],
                                                     offset[1]+ (self.current_sprites[round(self.animation_frame)].get_height() // 1.2)))

        # draw current sprite(s)
        SCREEN.blit(self.current_sprites[round(self.animation_frame)], offset)

        pygame.draw.rect(SCREEN, (000, 000, 000), self.rect)

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
            self.row_8_to_9 = True
        elif self.rect.bottom < (borders[7]["upper"] - (calc_diff_vertically(7, 8) / 3)) and self.row_7_to_8 != True:
            switch_tile()
            self.current_row = 8
            self.row_7_to_8 = True
        elif self.rect.bottom < (borders[6]["upper"] - (calc_diff_vertically(6, 7) / 4)) and self.row_6_to_7 != True:
            switch_tile()
            self.current_row = 7
            self.row_6_to_7 = True
        elif self.rect.bottom < (borders[5]["upper"] - (calc_diff_vertically(5, 6) / 4)) and self.row_5_to_6 != True:
            switch_tile()
            self.current_row = 6
            self.row_5_to_6 = True
        elif self.rect.bottom < (borders[4]["upper"] - (calc_diff_vertically(4, 5) / 4)) and self.row_4_to_5 != True:
            switch_tile()
            self.current_row = 5
            self.row_4_to_5 = True
        elif self.rect.bottom < (borders[3]["upper"] - (calc_diff_vertically(3, 4) / 4)) and self.row_3_to_4 != True:
            switch_tile()
            self.current_row = 4
            self.row_3_to_4 = True
        elif self.rect.bottom < (borders[2]["upper"] - (calc_diff_vertically(2, 3) / 4)) and self.row_2_to_3 != True:
            switch_tile()
            self.current_row = 3
            self.row_2_to_3 = True
        elif self.rect.bottom < (borders[1]["upper"] - (calc_diff_vertically(1, 2) / 4)) and self.row_1_to_2 != True:
            switch_tile()
            self.current_row = 2
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
                case 1: self.x += 0.7 if self.current_row < 6 else 0.6
                case 2: self.x += 0.6 if self.current_row < 6 else 0.5
                case 3: self.x += 0.5 if self.current_row < 6 else 0.4
                case 5: self.x -= 0.5 if self.current_row < 6 else 0.4
                case 6: self.x -= 0.6 if self.current_row < 6 else 0.5
                case 7: self.x -= 0.7 if self.current_row < 6 else 0.6

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

        self.pos = (self.x, self.y)

    def update(self):
        self.load_rect()
        self.move()
        self.record_my_path(self.current_tile)
        self.draw()

