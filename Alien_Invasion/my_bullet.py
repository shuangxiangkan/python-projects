import pygame
from pygame.sprite import Sprite


class My_bullet(Sprite):

    def __init__(self,setting,ship,screen):
        super().__init__()
        # self.setting=setting
        self.screen=screen

        # self.rect=pygame.rect(0,0,setting.bullet_width,setting.bullet_height)
        self.rect=pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.color=setting.bullet_color
        self.y=self.rect.y
        self.rect_speed_factor=setting.bullet_speed_factor


    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

    def update(self):
        self.y-=self.rect_speed_factor
        self.rect.y=self.y

