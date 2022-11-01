
from main import pygame, SCREEN, random
from fonts import FONT_PRESS_START_30


class PressSpace:
    def __init__(self):
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
        SCREEN.fill("black")
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
            self.__init__()
            self.screen_done = True


