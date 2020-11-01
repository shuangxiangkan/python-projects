import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, setting,screen,ship):
        super().__init__()
        self.setting = setting
        self.ship=ship
        self.screen=screen

        # Create a bullet at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, setting.bullet_width, setting.bullet_height)
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top


    def update(self):
        self.rect.y-=self.setting.bullet_speed_factor


    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.setting.bullet_color,self.rect)

