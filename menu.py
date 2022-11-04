
from main import pygame, SCREEN, random
from fonts import FONT_PRESS_START_20, FONT_PRESS_START_30

import time

#-----MENU SFX-----#
sfx_menu_move =pygame.mixer.Sound("sfx/menu/menu_move.wav")
sfx_menu_move.set_volume(0.5)

sfx_pressed_space = pygame.mixer.Sound("sfx/menu/pressed_space.wav")
sfx_pressed_space.set_volume(0.6)

sfx_screen_done = pygame.mixer.Sound("sfx/menu/screen_done.wav")
sfx_screen_done.set_volume(0.6)

sfx_char_selected = pygame.mixer.Sound("sfx/menu/char_selected.wav")
sfx_char_selected.set_volume(0.6)

class PressSpace:
    def __init__(self, menu_screen):
        self.menu_screen = menu_screen
        self.key_pressed = False
        self.key_pressed_timestamp = time.time()
        self.font = FONT_PRESS_START_30
        self.left_gate_pos = pygame.math.Vector2(x=0, y=0)
        self.right_gate_pos = pygame.math.Vector2(x=46, y=16)
        self.left_gate_done = False
        self.right_gate_done = False
        self.load_graphics()
        self.load_rects()
        self.start_gate_animation = False
        self.font_animation_counter = 0
        self.logo_animation_counter = 0
        self.logo_animation_forward = True
        self.correct_konami_code_keys = ["U", "U", "D", "D", "L", "R", "L", "R", "B", "A"]
        self.konami_code_keys = []
        self.konami_code = False
        self.screen_done = False

    def load_graphics(self):
        self.left_gate = pygame.image.load("graphics/menu/press_space/press_space_left.png").convert_alpha()
        self.right_gate = pygame.image.load("graphics/menu/press_space/press_space_right.png").convert_alpha()

        self.logo_frames = []
        for i in range(8):
            self.logo_frames.append(pygame.image.load(f"graphics/menu/press_space/logo_f{i+1}.png").convert_alpha())

        self.font_surf = self.font.render("PRESS SPACE", False, (252, 252, 252))

    def load_rects(self):
        self.left_gate_rect = self.left_gate.get_rect(topleft=self.left_gate_pos)
        self.right_gate_rect = self.right_gate.get_rect(topleft=self.right_gate_pos)

        self.logo_rect = self.logo_frames[0].get_rect(center=(400, 200))

        self.font_rect = self.font_surf.get_rect(center=(400, 480))

    def event_listen(self):

        def stamp_time_key_press():
            self.key_pressed = True
            self.key_pressed_timestamp = time.time()

        if self.key_pressed != True:
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_SPACE]:
                self.start_gate_animation = True
                sfx_pressed_space.play()
                stamp_time_key_press()
            elif self.keys[pygame.K_UP]:
                self.konami_code_keys.append("U")
                stamp_time_key_press()
            elif self.keys[pygame.K_DOWN]:
                self.konami_code_keys.append("D")
                stamp_time_key_press()
            elif self.keys[pygame.K_LEFT]:
                self.konami_code_keys.append("L")
                stamp_time_key_press()
            elif self.keys[pygame.K_RIGHT]:
                self.konami_code_keys.append("R")
                stamp_time_key_press()
            elif self.keys[pygame.K_a]:
                self.konami_code_keys.append("A")
                stamp_time_key_press()
            elif self.keys[pygame.K_b]:
                self.konami_code_keys.append("B")
                stamp_time_key_press()
        else:
            if round(time.time(), 1) > round(self.key_pressed_timestamp, 1)+0.2 and self.start_gate_animation != True:
                self.key_pressed = False

    def font_animation(self):
        self.font_animation_counter += 0.02

        if round(self.font_animation_counter) > 1:
            self.font_animation_counter = 0

        if round(self.font_animation_counter) == 0:
            SCREEN.blit(self.font_surf, self.font_rect)

    def gate_animation(self):
        if self.start_gate_animation:
            if self.left_gate_rect.right > 0:
                self.left_gate_pos.x -= 10
            else:
                self.left_gate_done = True
            if self.right_gate_rect.left < 800:
                self.right_gate_pos.x += 10
            else:
                self.right_gate_done = True

    def logo_animation(self):

        if round(self.logo_animation_counter + 0.2) > 7:
            self.logo_animation_forward = False
        elif round(self.logo_animation_counter - 0.2) < 0:
            self.logo_animation_forward = True

        if self.logo_animation_forward:
            self.logo_animation_counter += 0.2
        else:
            self.logo_animation_counter -= 0.2

    def check_if_konami_code(self):

        if self.konami_code != True:
            corr_keys = 0

            possible_konami_code = []

            for key in self.konami_code_keys:

                if corr_keys == 0:
                    if key == self.correct_konami_code_keys[0]:
                        possible_konami_code.append(key)
                        corr_keys += 1
                elif corr_keys == 1:
                    if key == self.correct_konami_code_keys[1]:
                        possible_konami_code.append(key)
                        corr_keys += 1
                elif corr_keys == 2:
                    if key == self.correct_konami_code_keys[2]:
                        possible_konami_code.append(key)
                        corr_keys += 1
                elif corr_keys == 3:
                    if key == self.correct_konami_code_keys[3]:
                        possible_konami_code.append(key)
                        corr_keys += 1
                elif corr_keys == 4:
                    if key == self.correct_konami_code_keys[4]:
                        possible_konami_code.append(key)
                        corr_keys += 1
                elif corr_keys == 5:
                    if key == self.correct_konami_code_keys[5]:
                        possible_konami_code.append(key)
                        corr_keys += 1
                elif corr_keys == 6:
                    if key == self.correct_konami_code_keys[6]:
                        possible_konami_code.append(key)
                        corr_keys += 1
                elif corr_keys == 7:
                    if key == self.correct_konami_code_keys[7]:
                        possible_konami_code.append(key)
                        corr_keys += 1
                elif corr_keys == 8:
                    if key == self.correct_konami_code_keys[8]:
                        possible_konami_code.append(key)
                        corr_keys += 1
                elif corr_keys == 9:
                    if key == self.correct_konami_code_keys[9]:
                        possible_konami_code.append(key)
                        corr_keys += 1
                else:
                    corr_keys = 0
                    possible_konami_code = []

                if self.correct_konami_code_keys == possible_konami_code:
                    self.konami_code = True
                    break

    def draw(self):

        if self.start_gate_animation:
            self.menu_screen.update()

        # left gate
        SCREEN.blit(self.left_gate, self.left_gate_rect)
        # right gate
        SCREEN.blit(self.right_gate, self.right_gate_rect)

        # game logo
        self.logo_animation()
        SCREEN.blit(self.logo_frames[round(self.logo_animation_counter)], self.logo_rect)

    def check_if_done(self):
        if self.left_gate_done and self.right_gate_done:
            return True
        else:
            return False

    def update(self):
        self.event_listen()
        self.load_rects()
        self.gate_animation()
        self.draw()
        self.font_animation()

        if len(self.konami_code_keys) >= 10:
            self.check_if_konami_code()

        if self.check_if_done():
            # self.__init__(self.menu_screen)
            self.screen_done = True


class MenuScreen:
    def __init__(self):
        self.current_screen = "numb_of_players"
        self.font = FONT_PRESS_START_20
        self.FONT_COLOR_WHITE = (252, 252, 252)
        self.FONT_COLOR_RED = (173, 26, 26)
        self.load_graphics()
        self.key_pressed = False
        self.key_pressed_timestamp = time.time()
        self.menu_pane_pos = pygame.math.Vector2(75, 300)
        self.MENU_PANE_START_HEIGHT = 2
        self.MENU_PANE_END_HEIGHT = 350
        self.menu_pane_height = self.MENU_PANE_START_HEIGHT
        self.start_menu_pane_animation = False
        self.show_buttons = False
        self.menu_pane_direct = "on"
        self.numb_of_players = 1
        self.current_player = "mar"
        self.players = []
        self.last_player_selection_timestamp = 0
        self.screen_done = False
        self.restart_game = False

    def load_graphics(self):
        # bg image
        self.bg = pygame.image.load("graphics/menu/menu_screen/bg.png")

        # chains
        self.chains = []
        for i in range(7):
            self.chains.append(pygame.image.load("graphics/menu/menu_screen/chain.png").convert_alpha())

        # chains xy-pos
        self.chains_pos = [
            pygame.math.Vector2(64, -10),
            pygame.math.Vector2(159, -10),
            pygame.math.Vector2(272, -10),
            pygame.math.Vector2(405, -10),
            pygame.math.Vector2(535, -10),
            pygame.math.Vector2(659, -10),
            pygame.math.Vector2(762, -10)
        ]

        self.rotate_angles = []
        for i in range(7):
            self.rotate_angles.append(random.randint(-2, 2))
        self.swing = True

        # player select images
        self.player_select_images = {}
        self.player_select_pos = {}
        for player in ["mar", "lui", "pea", "yos"]:
            self.player_select_images[player] = []
            for i in range(1, 3):
                self.player_select_images[player].append(pygame.image.load(f"graphics/player/{player}/player_select/{player}_player_select_f{i}.png"))

            match player:
                case "mar": self.player_select_pos[player] = pygame.math.Vector2(x=147, y=157)
                case "lui": self.player_select_pos[player] = pygame.math.Vector2(x=453, y=157)
                case "pea": self.player_select_pos[player] = pygame.math.Vector2(x=147, y=331)
                case "yos": self.player_select_pos[player] = pygame.math.Vector2(x=453, y=331)

        # player controls
        self.player_controls_images = {}
        self.player_controls_pos = {}
        for i in range(1, 5):
            self.player_controls_images[i] = pygame.image.load(f"graphics/menu/controls/controls_p{i}.png").convert_alpha()

            match i:
                case 1: self.player_controls_pos[i] = pygame.math.Vector2(x=80, y=185)
                case 2: self.player_controls_pos[i] = pygame.math.Vector2(x=242, y=245)
                case 3: self.player_controls_pos[i] = pygame.math.Vector2(x=403, y=185)
                case 4: self.player_controls_pos[i] = pygame.math.Vector2(x=565, y=245)

        # menu fonts
        # numb_of_players
        font_surf_1p = self.font.render("1 PLAYER", False, self.FONT_COLOR_WHITE)
        font_surf_2p = self.font.render("2 PLAYERS", False, self.FONT_COLOR_WHITE)
        font_surf_3p = self.font.render("3 PLAYERS", False, self.FONT_COLOR_WHITE)
        font_surf_4p = self.font.render("4 PLAYERS", False, self.FONT_COLOR_WHITE)
        font_rect_1p = font_surf_1p.get_rect(center=(400, 164))
        font_rect_2p = font_surf_2p.get_rect(center=(400, 251))
        font_rect_3p = font_surf_3p.get_rect(center=(400, 338))
        font_rect_4p = font_surf_4p.get_rect(center=(400, 425))

        # player_select
        font_surf_p1 = self.font.render("P1", False, self.FONT_COLOR_WHITE)
        font_surf_p2 = self.font.render("P2", False, self.FONT_COLOR_WHITE)
        font_surf_p3 = self.font.render("P3", False, self.FONT_COLOR_WHITE)
        font_surf_p4 = self.font.render("P4", False, self.FONT_COLOR_WHITE)

        self.fonts = {
            "numb_of_players" : {
                1 : [font_surf_1p, font_rect_1p],
                2 : [font_surf_2p, font_rect_2p],
                3 : [font_surf_3p, font_rect_3p],
                4 : [font_surf_4p, font_rect_4p]
            },
            "player_select" : {
                1 : [font_surf_p1],
                2 : [font_surf_p2],
                3 : [font_surf_p3],
                4 : [font_surf_p4]
            }
        }

    def load_player_positions(self, player_end_positions:list):

        self.player_pos_fonts = {
            1 : [],
            2 : [],
            3 : [],
            4 : []
        }

        for pos in range(len(player_end_positions)):

            match pos:
                case 0: coord = (400, 164); pos_text = "1st: "
                case 1: coord = (400, 251); pos_text = "2nd: "
                case 2: coord = (400, 338); pos_text = "3rd: "
                case 3: coord = (400, 425); pos_text = "4th: "

            self.player_pos_fonts[pos + 1].append(self.font.render(f"{pos_text}P{player_end_positions[pos]}", False, self.FONT_COLOR_WHITE))
            self.player_pos_fonts[pos+1].append(self.player_pos_fonts[pos+1][0].get_rect(center=coord))

    def event_listen(self):

        def stamp_time_key_press():
            self.key_pressed = True
            self.key_pressed_timestamp = time.time()

        if self.key_pressed != True:
            self.keys = pygame.key.get_pressed()

            if self.keys[pygame.K_RETURN]:
                if self.current_screen == "numb_of_players":
                    self.current_screen = "player_select"
                    self.menu_pane_direct = "off"
                    sfx_screen_done.play()
                elif self.current_screen == "player_select" and len(self.players) < 4:
                    if len(self.players) < 3:
                        self.players.append(self.current_player)
                        sfx_char_selected.play()
                    else:
                        self.players.append(self.current_player)
                        sfx_char_selected.play()
                        self.last_player_selection_timestamp = time.time()
                        self.menu_pane_direct = "off"
                    x_offset = 5
                    if self.players.count(self.current_player) > 1:
                        x_offset += (self.players.count(self.current_player) * 50) - 50
                    pnum_pos = (self.player_select_pos[self.current_player].x + x_offset, self.player_select_pos[self.current_player].y + 5)
                    if len(self.fonts["player_select"][len(self.players)]) > 1:
                        self.fonts["player_select"][len(self.players)].pop()
                    self.fonts["player_select"][len(self.players)].append(self.fonts["player_select"][len(self.players)][0].get_rect(topleft=pnum_pos))
                elif self.current_screen == "controls":
                    self.menu_pane_direct = "off"
                    sfx_screen_done.play()
                elif self.current_screen == "positions":
                    self.menu_pane_direct = "off"
                    sfx_screen_done.play()
                stamp_time_key_press()
            elif self.keys[pygame.K_ESCAPE]:
                self.players.clear()
            elif self.keys[pygame.K_UP]:
                if self.current_screen == "numb_of_players":
                    if self.numb_of_players > 1:
                        self.numb_of_players -= 1
                        sfx_menu_move.play()
                elif self.current_screen == "player_select":
                    if self.current_player == "pea":
                        self.current_player = "mar"
                        sfx_menu_move.play()
                    elif self.current_player == "yos":
                        self.current_player = "lui"
                        sfx_menu_move.play()
                stamp_time_key_press()
            elif self.keys[pygame.K_DOWN]:
                if self.current_screen == "numb_of_players":
                    if self.numb_of_players < 4:
                        self.numb_of_players += 1
                        sfx_menu_move.play()
                elif self.current_screen == "player_select":
                    if self.current_player == "mar":
                        self.current_player = "pea"
                        sfx_menu_move.play()
                    elif self.current_player == "lui":
                        self.current_player = "yos"
                        sfx_menu_move.play()
                stamp_time_key_press()
            elif self.keys[pygame.K_RIGHT]:
                if self.current_screen == "player_select":
                    if self.current_player == "mar":
                        self.current_player = "lui"
                        sfx_menu_move.play()
                    elif self.current_player == "pea":
                        self.current_player = "yos"
                        sfx_menu_move.play()
                stamp_time_key_press()
            elif self.keys[pygame.K_LEFT]:
                if self.current_screen == "player_select":
                    if self.current_player == "lui":
                        self.current_player = "mar"
                        sfx_menu_move.play()
                    elif self.current_player == "yos":
                        self.current_player = "pea"
                        sfx_menu_move.play()
                stamp_time_key_press()

        else:
            if round(time.time(), 1) > round(self.key_pressed_timestamp, 1)+0.2:
                self.key_pressed = False

    def load_menu_pane_rect(self):
        self.menu_pane_rect = pygame.Rect(self.menu_pane_pos.x, self.menu_pane_pos.y, 650, self.menu_pane_height)
        self.menu_pane_surf = pygame.Surface((650, self.menu_pane_height))
        self.menu_pane_surf.fill((100, 54, 135))
        self.menu_pane_surf.set_alpha(180)

    def animate_menu_pane(self, direct:str):
        if direct == "on":
            if self.menu_pane_height + 30 <= self.MENU_PANE_END_HEIGHT:
                self.menu_pane_height += 30
                self.menu_pane_pos.y -= 15
            else:
                self.show_buttons = True
        else:
            if self.last_player_selection_timestamp == 0 or (self.last_player_selection_timestamp > 0 and self.last_player_selection_timestamp + 0.5 < time.time()):
                self.show_buttons = False
                if self.menu_pane_height - 30 >= self.MENU_PANE_START_HEIGHT:
                    self.menu_pane_height -= 30
                    self.menu_pane_pos.y += 15
                else:
                    self.menu_pane_direct = "on"
                    if self.current_screen == "player_select" and len(self.players) >= 4:
                        self.current_screen = "controls"
                        sfx_screen_done.play()
                    elif self.current_screen == "controls":
                        self.screen_done = True
                    elif self.current_screen == "positions":
                        self.restart_game = True
                    self.start_menu_pane_animation = True

    def draw_buttons(self):
        if self.current_screen == "numb_of_players":
            def reset_font_colot(player_numb):
                self.fonts[self.current_screen][player_numb][0] = self.font.render(f"{player_numb} {'PLAYER' if player_numb < 2 else 'PLAYERS'}", False, self.FONT_COLOR_WHITE)

            # re-colorize all number of player fonts white
            for i in range(1, 5):
                reset_font_colot(i)

            # colorize font of current player number position red
            self.fonts[self.current_screen][self.numb_of_players][0] = self.font.render(f"{self.numb_of_players} {'PLAYER' if self.numb_of_players < 2 else 'PLAYERS'}", False, self.FONT_COLOR_RED)

            for i in range(1, 5):
                SCREEN.blit(self.fonts[self.current_screen][i][0], self.fonts[self.current_screen][i][1])

        elif self.current_screen == "player_select":

            # draw player portraits f1
            for player in ["mar", "lui", "pea", "yos"]:
                SCREEN.blit(self.player_select_images[player][0], self.player_select_pos[player])

            # draw player portraits f2
            if len(self.players) > 0:
                for player in self.players:
                    SCREEN.blit(self.player_select_images[player][1], self.player_select_pos[player])

                # draw chosen player number on portrait
                for pnum in range(1, len(self.players)+1):
                    SCREEN.blit(self.fonts["player_select"][pnum][0], self.fonts["player_select"][pnum][1])

            # draw player select rectangle
            pygame.draw.rect(surface=SCREEN, color=(252, 252, 252), rect=pygame.Rect(int(self.player_select_pos[self.current_player].x), int(self.player_select_pos[self.current_player].y), 200, 100), width=4)

        elif self.current_screen == "controls":

            for i in range(1, self.numb_of_players + 1):
                SCREEN.blit(self.player_controls_images[i], self.player_controls_pos[i])

        elif self.current_screen == "positions":

            for i in range(1, 5):
                SCREEN.blit(self.player_pos_fonts[i][0], self.player_pos_fonts[i][1])

    def draw(self):
        # bg
        SCREEN.blit(self.bg, (0, 0))

        # chains
        for i in range(7):
            rotated_chain = pygame.transform.rotate(self.chains[i], round(self.rotate_angles[i]))
            rotated_chain_rect = rotated_chain.get_rect(center=self.chains[i].get_rect(topleft=self.chains_pos[i]).center)
            SCREEN.blit(rotated_chain, rotated_chain_rect)

            if self.rotate_angles[i] > 2:
                self.swing = False
            elif self.rotate_angles[i] < -2:
                self.swing = True

            if self.swing:
                self.rotate_angles[i] += 0.08
            else:
                self.rotate_angles[i] -= 0.08

        # menu pane
        if self.start_menu_pane_animation:
            self.load_menu_pane_rect()
            self.animate_menu_pane(self.menu_pane_direct)
            SCREEN.blit(self.menu_pane_surf, self.menu_pane_rect)

        if self.show_buttons:
            self.draw_buttons()

    def update(self):
        self.event_listen()
        self.draw()
