
from main import pygame, SCREEN

class Camera:
    def __init__(self, stage, player):
        self.stage = stage
        self.player = player

    def center_target_camera(self, target):
        self.stage.offset.x = target.rect.centerx - 200
        self.stage.offset.y = target.rect.centery - 290

    def draw(self):
        self.center_target_camera(self.player)
        self.stage.draw_elements()
        self.player.update()