
import random
from main import pygame, SCREEN


class Stage:
    def __init__(self):
        self.load_elements()
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

        draw_bg()
        draw_trails()
        draw_neon_signs()
        draw_chains()
        draw_tower()
        draw_piranha_plants()
        draw_tiles()


class ShyGuy:
    def __init__(self):
        self.sprites = self.load_sprites()
        self.x = 365
        self.y = 520
        self.animation_frame = 1
        self.current_dir = "stand_down" # je nach Bewegungsrichtung aendert sich die current_dir

    def load_sprites(self) -> dict:

        run_left = {
            1: "",
            2: "",
            3: "",
            4: "",
        }

        run_right = {
            1: "",
            2: "",
            3: "",
            4: ""
        }

        run_up = {
            1: "",
            2: "",
            3: "",
            4: ""
        }

        stand_down = {
            1: "",
            2: ""
        }

        stand_left = {
            1: "",
            2: ""
        }

        stand_right = {
            1: "",
            2: ""
        }

        stand_up = {
            1: "",
            2: ""
        }

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
            if self.animation_frame + 0.1 > 4:
                self.animation_frame = 1
            else: self.animation_frame += 0.1
        else:
            if self.animation_frame + 0.07 > 2:
                self.animation_frame = 1
            else: self.animation_frame += 0.07

    def draw_sprites(self):

        # draw shadow
        SCREEN.blit(self.sprites["shadow"], (self.x, self.y+60))

        self.animation()
        SCREEN.blit(self.sprites["stand_down"][round(self.animation_frame)], (self.x, self.y))

