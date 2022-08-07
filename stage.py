
from main import pygame, SCREEN


class Stage:
    def __init__(self):
        self.load_elements()

    def load_elements(self):
        # load-sub-methods for loading graphic assets with xy-positions
        def load_bg():
            self.bg = pygame.image.load("graphics/stage/bg/background.png").convert_alpha()

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

        def load_neon_signs():
            # left signs

            self.bullet_bills = {
                1: pygame.image.load("graphics/stage/neon_signs/left/bullet_bills/bullet_bills_f1.png").convert_alpha(),
                2: pygame.image.load("graphics/stage/neon_signs/left/bullet_bills/bullet_bills_f2.png").convert_alpha()
            }

            self.vote_for_koopa = {
                1: pygame.image.load(
                    "graphics/stage/neon_signs/left/vote_for_koopa/vote_for_koopa_f1.png").convert_alpha(),
                2: pygame.image.load(
                    "graphics/stage/neon_signs/left/vote_for_koopa/vote_for_koopa_f2.png").convert_alpha()
            }

            # right signs

            self.fire_snake = {
                1: pygame.image.load("graphics/stage/neon_signs/right/fire_snake/fire_snake_f1.png").convert_alpha(),
                2: pygame.image.load("graphics/stage/neon_signs/right/fire_snake/fire_snake_f2.png").convert_alpha()
            }

            self.parts = {
                1: pygame.image.load("graphics/stage/neon_signs/right/parts/parts_f1.png").convert_alpha(),
                2: pygame.image.load("graphics/stage/neon_signs/right/parts/parts_f1.png").convert_alpha()
            }

        def load_piranha_plants():
            # left plant

            self.piranha_plant_left = {}

            for i in range(3):
                self.piranha_plant_left.update({i + 1: pygame.image.load(
                    f"graphics/stage/piranha_plants/left/piranha_plant_left_f{i + 1}.png").convert_alpha()})

            # right plant

            self.piranha_plant_right = {}

            for i in range(3):
                self.piranha_plant_right.update({i + 1: pygame.image.load(
                    f"graphics/stage/piranha_plants/right/piranha_plant_right_f{i + 1}.png").convert_alpha()})

        def load_tiles():
            # key = tile no : value = tile graphic

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
            self.tiles_corr = load_tiles_loop(self.tiles_corr, "corr")

        def load_tower():
            self.tower = {
                1: pygame.image.load("graphics/stage/tower/tower_f1.png").convert_alpha(),
                2: pygame.image.load("graphics/stage/tower/tower_f2.png").convert_alpha()
            }

        def load_trails():
            self.trails = pygame.image.load("graphics/stage/trails/trails.png").convert_alpha()

        # call of sub-methods for loading graphic assets
        load_bg()
        load_chains()
        load_neon_signs()
        load_piranha_plants()
        load_tiles()
        load_tower()
        load_trails()


