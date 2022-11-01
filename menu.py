
from main import pygame, SCREEN, random
from fonts import FONT_PRESS_START_30


class PressSpace:
    def __init__(self, menu_numb_of_players):
        self.menu_numb_of_players = menu_numb_of_players
        self.key_pressed = False
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
        if self.key_pressed != True:
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_SPACE]:
                self.start_gate_animation = True
                self.key_pressed = True

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


    def draw(self):

        if self.start_gate_animation:
            self.menu_numb_of_players.update()

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

        if self.check_if_done():
            self.__init__(self.menu_numb_of_players)
            self.screen_done = True


class NumbOfPlayers:
    def __init__(self):
        self.load_graphics()
        self.key_pressed = False
        self.menu_pane_pos = pygame.math.Vector2(75, 300)
        self.MENU_PANE_START_HEIGHT = 2
        self.MENU_PANE_END_HEIGHT = 350
        self.menu_pane_height = self.MENU_PANE_START_HEIGHT
        self.start_menu_pane_animation = False
        self.menu_pane_direct = "on"
        self.screen_done = False

    def load_graphics(self):
        self.bg = pygame.image.load("graphics/menu/numb_of_players/bg.png")
        self.chains = []
        for i in range(7):
            self.chains.append(pygame.image.load("graphics/menu/numb_of_players/chain.png").convert_alpha())
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

    def event_listen(self):
        if self.key_pressed != True:
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_RETURN]:
                self.menu_pane_direct = "off"
                self.key_pressed = True

    def load_menu_pane_rect(self):
        self.menu_pane_rect = pygame.Rect(self.menu_pane_pos.x, self.menu_pane_pos.y, 650, self.menu_pane_height)
        self.menu_pane_surf = pygame.Surface((650, self.menu_pane_height))
        self.menu_pane_surf.fill((100, 54, 135))
        self.menu_pane_surf.set_alpha(180)

    def animate_menu_pane(self, direct):
        if direct == "on":
            if self.menu_pane_height + 30 <= self.MENU_PANE_END_HEIGHT:
                self.menu_pane_height += 30
                self.menu_pane_pos.y -= 15
        else:
            if self.menu_pane_height - 30 >= self.MENU_PANE_START_HEIGHT:
                self.menu_pane_height -= 30
                self.menu_pane_pos.y += 15

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
            # pygame.draw.rect(SCREEN, (100, 54, 135), self.menu_pane_rect)

    def update(self):
        self.event_listen()
        self.draw()
